import h5py  # type: ignore
import pandas as pd
from collections import OrderedDict
import numpy as np
import itertools


def get_df(
    hdf: h5py.File,
    value: str,
    keys: list[str] = ["technology", "carrier", "node", "time_step"],
) -> pd.DataFrame:
    current_df = {key: val for key, val in hdf[value]["dataframe"].items()}

    index_set = OrderedDict()

    n_data = len(current_df["block0_values"][:, 0])

    for j, key in enumerate(keys):
        current_level = "axis1_level" + str(j)
        if current_level not in current_df:
            current_df[current_level] = list(range(n_data))
            current_df[current_level.replace("level", "label")] = list(range(n_data))
        index_set[key] = [i for i in set(current_df[current_level])]

    index_list = [index_set[i] for i in index_set]
    indices = list(itertools.product(*index_list))
    pandas_index = pd.MultiIndex.from_tuples(indices, names=keys)
    data_matrix = np.empty(len(indices))
    data_matrix[:] = np.nan
    dataframe: pd.DataFrame = pd.DataFrame(data_matrix, index=pandas_index)
    label_strings = [f"axis1_label{j}" for j in range(len(keys))]
    level_strings = [f"axis1_level{j}" for j in range(len(keys))]
    index: list[bytes] = [b"" for _ in keys]
    print(f"Loading {value} with {n_data} data points")
    for i in range(n_data):
        for j in range(len(keys)):
            current_level_index = current_df[label_strings[j]][i]
            current_key = current_df[level_strings[j]][current_level_index]
            index[j] = current_key
        tuple_index = tuple(index)
        dataframe.loc[tuple_index] = current_df["block0_values"][i, 0]

    return dataframe.astype(pd.SparseDtype("float", np.nan))
