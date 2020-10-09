import json
import os

import pandas as pd

# -------------------- #
def simple_example():
    records = [('Espresso', '5$'), ('Flat White', '10$')]
    print(pd.DataFrame.from_records(records))
    print(pd.DataFrame.from_records(records, columns=['Coffee', 'Price']))


KEYS = [
    'id',
    'all_artists',
    'title',
    'medium',
    'dateText',
    'acquisitionYear',
    'height',
    'width',
    'units',
]

# -------------------- #
def get_record_from_file(file_path, keys_to_use):
    with open(file_path) as artwork_file:
        content = json.load(artwork_file)

    record = []
    for field in keys_to_use:
        record.append(content[field])

    return tuple(record)


JSON_FILE = os.path.join(
    './', 'collection-master', 'artworks', 'a', '000', 'a00001-1035.json'
)

sample_record = get_record_from_file(JSON_FILE, KEYS)


# -------------------- #
def read_artworks_from_json(keys_to_use):
    JSON_ROOT = os.path.join('./', 'collection-master', 'artworks')

    artworks = []
    for root, _, files in os.walk(JSON_ROOT):
        for f in files:
            if f.endswith('json'):
                record = get_record_from_file(
                    os.path.join(root, f), keys_to_use
                )
                artworks.append(record)
            break

    df = pd.DataFrame.from_records(artworks, columns=KEYS, index='id')
    return df


_df = read_artworks_from_json(KEYS)
