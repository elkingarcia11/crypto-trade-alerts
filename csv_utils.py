import csv
import datetime
import pandas as pd

def get_last_datetime_from_csv(file_path):
    """
    Retrieves the last datetime from a CSV file containing financial data.

    Parameters:
        file_path (str): The path to the CSV file.

    Returns:
        datetime.datetime: The last datetime found in the CSV file.
    """
    df = pd.read_csv(file_path)
    last_datetime_str = df['Date'].iloc[-1]
    last_datetime = datetime.datetime.strptime(last_datetime_str, '%Y-%m-%d %H:%M:%S')
    return last_datetime

def save_to_csv(data, file_path, include_headers=False):
    """
    Saves data to a CSV file.

    Parameters:
        data (list of lists): The data to be saved.
        file_path (str): The path to the CSV file.
        include_headers (bool, optional): Whether to include headers in the CSV file. Defaults to False.

    Returns:
        None
    """
    headers = ['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
    mode = 'a' if not include_headers else 'w'
    with open(file_path, mode, newline='') as f:
        writer = csv.writer(f)
        if include_headers:
            writer.writerow(headers)
        for row in data:
            writer.writerow(row)
