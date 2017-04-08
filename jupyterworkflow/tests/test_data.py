import pandas as pd
from jupyterworkflow.data import get_fremont_data
import numpy as np

def test_fremont_data():
    df = get_fremont_data()
    assert(all(df.columns.values == ['West', 'East', 'Total']))
    assert(isinstance(df.index, pd.DatetimeIndex))
    assert(len(np.unique(df.index.time)) == 24)