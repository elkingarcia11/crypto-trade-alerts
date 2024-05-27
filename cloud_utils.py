import os
from google.cloud import storage

def fetch_data(ticker_symbol, key_path="service_account_credentials.json"):
    """
    Fetches the CSV file from Google Cloud Storage.

    Parameters:
        ticker_symbol (str): The symbol of the financial instrument for which to fetch the data.
        key_path (str, optional): The path to the service account credentials JSON file.
            Defaults to "service_account_credentials.json".

    Returns:
        None
    """
    storage_client = storage.Client.from_service_account_json(key_path)

    bucket_name = os.getenv('GOOGLE_CLOUD_BUCKET_NAME')
    if not bucket_name:
        raise ValueError("Bucket name is not set in the environment variable 'GOOGLE_CLOUD_BUCKET_NAME'")
    
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(f"{ticker_symbol}.csv")
    blob.download_to_filename(f"data/{ticker_symbol}.csv")

    print(f"File downloaded from bucket '{bucket_name}' to 'data/{ticker_symbol}.csv'.")

def upload_data(ticker_symbol):
    """
    Uploads the updated CSV file to Google Cloud Storage.

    Parameters:
        ticker_symbol (str): The symbol of the financial instrument for which to upload the data.

    Returns:
        str: A message confirming the successful upload.
    """
    key_path = "service_account_credentials.json"
    storage_client = storage.Client.from_service_account_json(key_path)

    bucket_name = os.getenv('GOOGLE_CLOUD_BUCKET_NAME')
    if not bucket_name:
        raise ValueError("Bucket name is not set in the environment variable 'GOOGLE_CLOUD_BUCKET_NAME'")
    
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(f"{ticker_symbol}.csv")
    blob.upload_from_filename(f'data/{ticker_symbol}.csv')

    return f"Data for {ticker_symbol} merged and uploaded to Cloud Storage."
