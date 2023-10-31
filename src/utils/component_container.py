import h5py  # type: ignore
import numpy.typing as npt
import numpy as np
from typing import Any
from ..models.solution import SeriesBehaviour, DataRequest, IndexSet
import itertools
import csv
import io
from typing import Optional
from pydantic import BaseModel
import os
import json
from zen_garden.model.default_config import System  # type: ignore


class LevelInfo(BaseModel):
    title: str
    names: list[str | int] = []


class ComponentInfo(BaseModel):
    component_name: str
    yearly: bool = False
    aggregated_time_steps_per_year: int = 1
    levels: list[LevelInfo] = []

    @staticmethod
    def from_path(path: str) -> "ComponentInfo":
        with open(path, "r") as f:
            ans = ComponentInfo(**json.load(f))
        return ans


class ComponentContainer:
    def __init__(self, data: npt.NDArray[np.float_], info: ComponentInfo):
        self.data: npt.NDArray[np.float_] = data
        self.info: ComponentInfo = info

    def save(self, path: str) -> None:
        if not os.path.exists(path):
            raise FileNotFoundError

        base_path = os.path.join(path, self.info.component_name)
        np.save(base_path + ".npy", self.data)

        with open(base_path + ".json", "w") as f:
            json.dump(self.info.dict(), f, indent=2)

    @staticmethod
    def load(component_name: str, path: str) -> "ComponentContainer":
        ndarray_path = os.path.join(path, component_name + ".npy")
        component_info_path = os.path.join(path, component_name + ".json")
        with open(component_info_path, "r") as f:
            json_data = json.load(f)
            component_info: ComponentInfo = ComponentInfo(**json_data)

        np_array: npt.NDArray[np.float_] = np.load(ndarray_path)
        return ComponentContainer(np_array, component_info)

    @staticmethod
    def create_from_hdf(
        hdf: h5py.File,
        component_name: str,
        system: System,
        keys: list[str] = ["technology", "carrier", "node", "time_step"],
        time_index: Optional[int] = None,
    ) -> "ComponentContainer":
        """Creates a n-dimensional numpy array from a hdf5 file.

        Arguments:
        hdf -- The hdf file to read
        component_name: which component of the hdf file (must be in the first keys)

        Keyword arguments:
        keys -- Names of the levels inside the hdf5 file
        """
        current_df = {key: val for key, val in hdf[component_name]["dataframe"].items()}
        component_info = ComponentInfo(component_name=component_name)
        component_info.levels = [LevelInfo(title=key) for key in keys]
        n_data = len(current_df["block0_values"][:, 0])

        if time_index is None:
            time_index = -1

        for j, key in enumerate(keys):
            current_level = "axis1_level" + str(j)
            if current_level not in current_df:
                current_df[current_level] = list(range(n_data))
                current_df[current_level.replace("level", "label")] = list(
                    range(n_data)
                )

            level_names = []

            for i in current_df[current_level]:
                try:
                    level_names.append(i.decode())
                except AttributeError:
                    level_names.append(int(i))

            component_info.levels[j].names = level_names

        data_size = tuple(len(i.names) for i in component_info.levels)
        ans = np.empty(data_size)
        ans[:] = np.nan
        label_strings = [f"axis1_label{j}" for j in range(len(keys))]
        index: list[int] = [-1 for _ in keys]
        print(f"Loading {component_name} with {n_data} data points")

        for i in range(n_data):
            for j in range(len(keys)):
                current_level_index = current_df[label_strings[j]][i]
                index[j] = current_level_index

            ans[tuple(index)] = current_df["block0_values"][i, 0]

        component_info.yearly = data_size[time_index] == system.optimized_years
        component_info.aggregated_time_steps_per_year = (
            system.aggregated_time_steps_per_year
        )
        return ComponentContainer(ans, component_info)

    def summarize_np_array(
        self,
        request: DataRequest,
        keep_dimensions: bool = False,
        nan_to_zeros: bool = False,
    ) -> "ComponentContainer":
        """Summarizes a given np array given the index of the numpy array and a
        DataRequest.

        Arguments:
        data -- Numpy Array
        component_info -- Information about the component
        request -- DataRequest (see documentation of DataRequest)
        """
        data = self.data
        component_info = self.info

        level_names = [i.title for i in component_info.levels]
        requested_level_names = [i.index_title for i in request.index_sets]
        initial_shape = data.shape

        non_existing_level_names = set(requested_level_names) - set(level_names)

        assert (
            len(non_existing_level_names) == 0
        ), f"The requested names {non_existing_level_names} are not part of the dataset (f{level_names})"

        for missing_name in set(level_names) - set(requested_level_names):
            new_set = IndexSet(
                index_title=missing_name, behaviour=request.default, indices=[]
            )
            request.index_sets.append(new_set)

        indices: list[list[int] | slice] = [[]] * len(level_names)

        for request_index in request.index_sets:
            index_in_numpy = level_names.index(request_index.index_title)
            if len(request_index.indices) > 0:
                current: list[int] | slice = [
                    component_info.levels[index_in_numpy].names.index(j)
                    for j in request_index.indices
                ]
            else:
                current = slice(0, initial_shape[index_in_numpy])

            indices[index_in_numpy] = current
        result = data.copy()

        for level, index in enumerate(indices):
            current_index: list[list[Any] | slice] = []
            current_shape = result.shape
            for i in range(len(level_names)):
                if i != level:
                    current_index.append(slice(0, current_shape[i]))
                else:
                    current_index.append(index)
            result = result[tuple(current_index)]

        # decide which of the indices need to be summed
        sum_indices = set(
            [
                level_names.index(i.index_title)
                for i in request.index_sets
                if i.behaviour == SeriesBehaviour.sum
            ]
        )

        if request.default == SeriesBehaviour.sum:
            default_sums = set(
                [
                    i
                    for i, name in enumerate(level_names)
                    if name not in requested_level_names
                ]
            )
            sum_indices = sum_indices.union(default_sums)

        list_sum_indices = list(sum_indices)
        list_sum_indices.sort()

        for i in list_sum_indices:
            if nan_to_zeros:
                result = np.nansum(result, axis=i, keepdims=True)
            else:
                result = np.sum(result, axis=i, keepdims=True)

        if not keep_dimensions:
            result = np.squeeze(result, axis=tuple(list_sum_indices))

        new_component_info: ComponentInfo = ComponentInfo(**component_info.dict())

        new_levels: list[LevelInfo] = []

        for key, old_index in enumerate(component_info.levels):
            if not keep_dimensions and key in sum_indices:
                continue
            current_keys = indices[key]
            new: list[str | int]
            if type(current_keys) is list:
                new = [old_index.names[i] for i in current_keys]
            elif type(current_keys) is slice:
                new = old_index.names[current_keys]
            else:
                new = []

            if key in sum_indices:
                new_str: list[str] = [str(i) for i in new]
                new = ["sum: " + ", ".join(new_str)]

            new_levels.append(LevelInfo(title=old_index.title, names=new))

        for i, size in enumerate(result.shape):
            assert len(new_levels[i].names) == size

        new_component_info.levels = new_levels

        return ComponentContainer(result, new_component_info)

    def aggregate_time_steps(
        self, time_index: Optional[int] = None, sequential: bool = False
    ) -> "ComponentContainer":
        data = self.data
        component_info = self.info

        n_steps_per_interval = self.info.aggregated_time_steps_per_year
        old_dim = data.shape
        if time_index is None:
            time_index = len(old_dim) - 1
        n_intervals = int(np.ceil(old_dim[time_index] / n_steps_per_interval))
        new_dim = [i for i in old_dim]
        new_dim[time_index] = n_intervals

        ans = np.zeros(new_dim)
        ans[:] = np.nan

        for i in range(n_intervals):
            index_list: list[slice | int | list[int]] = [
                slice(0, size) for i, size in enumerate(new_dim)
            ]

            # Create index in new ndarray
            index_list[time_index] = i
            single_index = tuple(index_list)

            # Create index of all timesteps to be summed
            if sequential:
                # Time steps are next to each other
                index_list[time_index] = slice(
                    i * n_steps_per_interval,
                    min((i + 1) * n_steps_per_interval, old_dim[time_index]),
                )
            else:
                # Years are next to each other
                index_list[time_index] = [
                    i + n_steps_per_interval * j for j in range(n_intervals)
                ]

            range_index = tuple(index_list)

            ans[single_index] = data[range_index].sum(axis=time_index)

        if component_info is not None:
            new_levels: list[LevelInfo] = [
                LevelInfo(**i.dict()) for i in component_info.levels
            ]
            new_levels[time_index].names = list(range(n_intervals))

            new_component_info = ComponentInfo(**component_info.dict())
            new_component_info.levels = new_levels

        return ComponentContainer(ans, new_component_info)

    def create_deep_csv(self) -> str:
        """
        Function creates a deep CSV file given a numpy array and the corresponding
        indices.
        """
        data = self.data
        component_info = self.info
        indices = itertools.product(*[i.names for i in component_info.levels])

        ans = io.StringIO()
        writer = csv.writer(ans)
        writer.writerow([i.title for i in component_info.levels] + ["value"])
        flat = data.flatten()
        skipped = 0
        for i, index in enumerate(indices):
            if np.isnan(flat[i]):
                skipped += 1
                continue
            writer.writerow(list(index) + [flat[i]])

        return ans.getvalue()
