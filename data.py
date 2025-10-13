import pandas as pd

def import_data(csv_file_path):
    dataframe = pd.read_csv(csv_file_path)
    return dataframe