import pandas as pd
import os

# Demo 1
df = pd.read_pickle(
    os.path.join('..', 'data_frame.pickle')
)  # it was created on demo_csv.py

artists = df['artist']
pd.unique(artists)
len(pd.unique(artists))


# Demo 2
s = artists == 'Bacon, Francis'

# Other way
artists_counts = artists.value_counts()
artists_counts['Bacon, Francis']


# Demo 3
df.loc[1035, 'artist']
df.iloc[0, 0]
df.iloc[0:2, 0:2]

# Try multiplication
df['height'] * df['width']  # error
df['width'].sort_values().head()
df['width'].sort_values().tail()

# Try to convert
pd.to_numeric(df['width'])  # error
pd.to_numeric(df['width'], errors='coerce')

df.loc[:, 'width'] = pd.to_numeric(df['width'], errors='coerce')
df.loc[:, 'height'] = pd.to_numeric(df['height'], errors='coerce')

df['height'] * df['width']

# Create nem Area colum (Assign)
area = df['height'] * df['width']
df = df.assign(area=area)

df['area'].max()
df['area'].idxmax()
df.loc[df['area'].idxmax(), :]
