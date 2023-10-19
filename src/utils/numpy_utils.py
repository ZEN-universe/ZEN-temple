import h5py  # type: ignore
import numpy.typing as npt
import numpy as np
from typing import Any
from ..models.solution import SeriesBehaviour, DataRequest, IndexSet
from collections import OrderedDict
import itertools
import csv
import io
from typing import Optional
from copy import deepcopy


IndexType = list[tuple[str, list[str | int]]]


def create_ndarray(
    hdf: h5py.File,
    value: str,
    keys: list[str] = ["technology", "carrier", "node", "time_step"],
) -> tuple[npt.NDArray[np.float_], IndexType]:
    """Creates a n-dimensional numpy array from a hdf5 file.

    Arguments:
    hdf -- The hdf file to read
    value: which component of the hdf file (must be in the first keys)

    Keyword arguments:
    keys -- Names of the levels inside the hdf5 file
    """
    current_df = {key: val for key, val in hdf[value]["dataframe"].items()}
    index_set = OrderedDict()

    n_data = len(current_df["block0_values"][:, 0])

    for j, key in enumerate(keys):
        current_level = "axis1_level" + str(j)
        if current_level not in current_df:
            current_df[current_level] = list(range(n_data))
            current_df[current_level.replace("level", "label")] = list(range(n_data))

        level_names = []

        for i in current_df[current_level]:
            try:
                level_names.append(i.decode())
            except AttributeError:
                level_names.append(int(i))

        index_set[key] = level_names

    data_size = tuple(len(i) for _, i in index_set.items())
    ans = np.empty(data_size)
    ans[:] = np.nan
    label_strings = [f"axis1_label{j}" for j in range(len(keys))]
    index: list[int] = [-1 for _ in keys]
    print(f"Loading {value} with {n_data} data points")

    for i in range(n_data):
        for j in range(len(keys)):
            current_level_index = current_df[label_strings[j]][i]
            index[j] = current_level_index

        ans[tuple(index)] = current_df["block0_values"][i, 0]

    return ans, [(key, val) for key, val in index_set.items()]


def summarize_np_array(
    data: npt.NDArray[np.float_],
    index_info: IndexType,
    request: DataRequest,
    keep_dimensions: bool = False,
    nan_to_zeros: bool = False,
) -> tuple[npt.NDArray[np.float_], IndexType]:
    """Summarizes a given np array given the index of the numpy array and a DataRequest.
    The index is of the form [(level_title, [level_names, ...]), ...].
    For example, if we have a Numpy-Array that contains two technologies "boiler" and "pv"
    and two nodes "CH" and "DE", the index info would be:

    [
        ("technology", ["boiler", "pv"]),
        ("node", ["CH", "DE"])
    ]

    Arguments:
    data -- Numpy Array
    index_info -- Index Information (see above)
    request -- DataRequest (see documentation of DataRequest)
    """
    index_names = [i[0] for i in index_info]
    requested_index_names = [i.index_title for i in request.index_sets]
    initial_shape = data.shape

    assert set(requested_index_names).issubset(set(index_names))

    for missing_name in set(index_names) - set(requested_index_names):
        new_set = IndexSet(
            index_title=missing_name, behaviour=request.default, indices=[]
        )
        request.index_sets.append(new_set)

    indices: list[list[int] | slice] = [[]] * len(index_names)

    for request_index in request.index_sets:
        index_in_numpy = index_names.index(request_index.index_title)
        if len(request_index.indices) > 0:
            current: list[int] | slice = [
                index_info[index_in_numpy][1].index(j) for j in request_index.indices
            ]
        else:
            current = slice(0, initial_shape[index_in_numpy])

        indices[index_in_numpy] = current
    result = data.copy()

    for level, index in enumerate(indices):
        current_index: list[list[Any] | slice] = []
        current_shape = result.shape
        for i in range(len(index_names)):
            if i != level:
                current_index.append(slice(0, current_shape[i]))
            else:
                current_index.append(index)
        result = result[tuple(current_index)]

    sum_indices = set(
        [
            index_names.index(i.index_title)
            for i in request.index_sets
            if i.behaviour == SeriesBehaviour.sum
        ]
    )

    if request.default == SeriesBehaviour.sum:
        default_sums = set(
            [
                i
                for i, name in enumerate(index_names)
                if name not in requested_index_names
            ]
        )
        sum_indices = sum_indices.union(default_sums)

    list_indices = list(sum_indices)
    list_indices.sort()

    for i in list_indices:
        if nan_to_zeros:
            result = np.nansum(result, axis=i, keepdims=keep_dimensions)
        else:
            result = np.sum(result, axis=i, keepdims=keep_dimensions)

    new_indices: IndexType = []
    for key, old_index in enumerate(index_info):
        if not keep_dimensions and key in sum_indices:
            continue
        current_keys = indices[key]
        new: list[str | int]
        if type(current_keys) is list:
            new = [old_index[1][i] for i in current_keys]
        elif type(current_keys) is slice:
            new = old_index[1][current_keys]
        else:
            new = []

        if key in sum_indices:
            new_str: list[str] = [str(i) for i in new]
            new = ["sum: " + ", ".join(new_str)]

        new_indices.append((old_index[0], new))

    for i, size in enumerate(result.shape):
        assert len(new_indices[i][1]) == size

    return result, new_indices


def aggregate_time_steps(
    data: npt.NDArray[np.float_],
    n_steps_per_interval: int,
    time_index: Optional[int] = None,
    index: Optional[IndexType] = None,
) -> tuple[npt.NDArray[np.float_], Optional[IndexType]]:
    old_dim = data.shape
    if time_index is None:
        time_index = len(old_dim) - 1
    n_intervals = int(np.ceil(old_dim[time_index] / n_steps_per_interval))
    new_dim = [i for i in old_dim]
    new_dim[time_index] = n_intervals

    ans = np.zeros(new_dim)
    ans[:] = np.nan

    for i in range(n_intervals):
        index_list: list[slice | int] = [
            slice(0, size) for i, size in enumerate(new_dim)
        ]
        index_list[time_index] = i
        single_index = tuple(index_list)
        index_list[time_index] = slice(
            i * n_steps_per_interval,
            min((i + 1) * n_steps_per_interval, old_dim[time_index]),
        )
        range_index = tuple(index_list)
        ans[single_index] = data[range_index].sum(axis=time_index)

    new_index: Optional[IndexType] = None
    if index is not None:
        new_index = deepcopy(index)
        new_index[time_index] = (new_index[time_index][0], list(range(n_intervals)))

    return ans, new_index


def create_deep_csv(data: npt.NDArray[np.float_], index_info: IndexType) -> str:
    """
    Function creates a deep CSV file given a numpy array and the corresponding indices.
    """
    indices = itertools.product(*[i[1] for i in index_info])
    print(data.shape)
    a = 1
    for i in data.shape:
        a *= i
    print(a)
    ans = io.StringIO()
    writer = csv.writer(ans)
    writer.writerow([i[0] for i in index_info] + ["value"])
    flat = data.flatten()
    for i, index in enumerate(indices):
        if np.isnan(flat[i]):
            continue
        writer.writerow(list(index) + [flat[i]])
    return ans.getvalue()
