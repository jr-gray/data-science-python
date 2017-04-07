import os
from urllib import urlretrieve
import pandas as pd

FREMONT_URL = 'https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD'

def get_fremont_data(filename='fremont.csv', url=FREMONT_URL, force_download=False):
    if force_download or not os.path.exists(filename):
        urlretrieve(url, filename)
    df = pd.read_csv('fremont.csv', index_col='Date', parse_dates=True)
    df.columns = ['West', 'East']
    df['Total'] = df['West'] + df['East']
    return df
