import pandas as pd
import numpy as np
from datetime import datetime
import os
from fastcore.basics import Path

def merge_label_files(label_folder):
    """
    Merges all label files in a given folder into a single pandas DataFrame. 
    The filenames must be in the format <ObjectID>.csv, and the object id will
    be extracted from the filename and added as a column to the DataFrame.

    Args:
        label_folder (str): The path to the folder containing the label files.

    Returns:
        pandas.DataFrame: A DataFrame containing the merged label data.
    """
    label_data = []
    label_folder = Path(label_folder).expanduser()
    for file_path in label_folder.ls():
        df = pd.read_csv(file_path)
        oid_s = os.path.basename(file_path).split('.')[0]  # Extract ObjectID from filename
        df['ObjectID'] = int(oid_s)
        label_data.append(df)

    label_data = pd.concat(label_data)
    label_data = label_data[['ObjectID'] + list(label_data.columns[:-1])]
    return label_data
