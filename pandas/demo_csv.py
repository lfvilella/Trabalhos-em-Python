import pandas as pd
import os

CSV_PATH = os.path.join('./', 'collection-master', 'artwork_data.csv')

COLS = [
    'id',
    'artist',
    'title',
    'medium',
    'year',
    'acquisitionYear',
    'height',
    'width',
    'units',
]

df = pd.read_csv(CSV_PATH, index_col='id', usecols=COLS)

df.to_pickle(os.path.join('./', 'data_frame.pickle'))
