import pathlib as path
import pandas as pd


def extract_data(file_path):

    file_path = path.Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    extension = file_path.suffix.lower()

    if extension == ".csv":
        return pd.read_csv(file_path)

    elif extension == ".xlsx":
        return pd.read_excel(file_path)

    elif extension == ".json":
        return pd.read_json(file_path)

    else:
        raise ValueError(f"Unsupported file type: {extension}")