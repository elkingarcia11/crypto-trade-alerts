import datetime

def format_data(data):
    """
    Converts data to a more readable format.

    Parameters:
        data (list of dicts): The data to be formatted, where each dictionary represents a data entry.

    Returns:
        list of lists: The formatted data, where each inner list contains the formatted data for a single entry.
            The format includes:
                - UTC datetime string
                - Open price
                - High price
                - Low price
                - Close price
                - Adjusted close price (assumed to be the same as Close)
                - Volume
    """
    formatted_data = []
    for entry in data:
        # Assume entry['time'] contains the timestamp
        timestamp = entry['time']

        # Format the timestamp to UTC datetime string
        utc_datetime_str = datetime.datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

        formatted_data.append([
            utc_datetime_str,
            entry['open'],
            entry['high'],
            entry['low'],
            entry['close'],
            entry['close'],  # Adj Close, assumed same as Close
            entry['volumeto']  # Assuming 'volumeto' is the relevant volume
        ])
    return formatted_data
