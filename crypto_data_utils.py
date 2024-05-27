import datetime
import csv_utils
import data_utils
import requests
import pytz

def fetch_latest_data(api_key, symbol="BTC", compare_currency="USD", limit=1, aggregate=1):
    """
    Fetches the last {LIMIT} data points for a cryptocurrency pair from an API.

    Parameters:
        api_key (str): API key for accessing the cryptocurrency data API.
        symbol (str, optional): The cryptocurrency symbol to fetch data for. Defaults to "BTC".
        compare_currency (str, optional): The currency to compare the cryptocurrency to. Defaults to "USD".
        limit (int, optional): Number of data points to fetch. Defaults to 1.
        aggregate (int, optional): Aggregation parameter for the API. Defaults to 1.

    Returns:
        list: A list of dictionaries containing the fetched data points.
    """
    url = "https://min-api.cryptocompare.com/data/v2/histohour"
    params = {
        'fsym': symbol,
        'tsym': compare_currency,
        'limit': limit,
        'aggregate': aggregate,
        'e': 'CCCAGG',
        'api_key': api_key
    }

    response = requests.get(url, params=params)
    data = response.json()

    if data["Response"] == "Success":
        return data['Data']['Data']
    else:
        raise Exception(f"Failed to fetch data: {data.get('Message', 'No error message')}")


def fetch_and_save_latest_data(ticker_symbol):
    """
    Fetches and saves latest data to csv file.

    Parameters:
        ticker_symbol (str): The symbol of the financial instrument to fetch and save data for.

    Returns:
        None
    """
    api_key = 'YOUR_API_KEY_HERE'  # Replace this with your actual API key
    try:
        # Get the last datetime from the CSV file
        csv_file_path = f"data/{ticker_symbol}.csv"

        # Get the last datetime from the CSV file (assume it's in UTC)
        last_datetime = csv_utils.get_last_datetime_from_csv(csv_file_path)
        last_datetime = last_datetime.replace(tzinfo=pytz.utc)  # Ensure timezone-aware in UTC

        # Get the current datetime in UTC (timezone-aware)
        new_datetime_utc = datetime.datetime.now(pytz.utc)

        # Calculate the difference in hours
        time_difference_hours = (new_datetime_utc - last_datetime).total_seconds() / 3600

        # Fetch the latest data
        raw_data = fetch_latest_data(api_key, limit=time_difference_hours)
        
        if raw_data:
            formatted_data = data_utils.format_data(raw_data)
            
            # Skip the first row to avoid duplicate entries
            formatted_data = formatted_data[1:]
            
            # Save to CSV
            csv_utils.save_to_csv(formatted_data, csv_file_path, include_headers=False)
        else:
            print("No data fetched.")
    except Exception as e:
        print(e)
