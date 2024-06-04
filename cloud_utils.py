import os
from google.cloud import storage
from dotenv import load_dotenv

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
    load_dotenv()
    bucket_name = os.getenv('GOOGLE_CLOUD_BUCKET_NAME')
    if not bucket_name:
        raise ValueError("Bucket name is not set in the environment variable 'GOOGLE_CLOUD_BUCKET_NAME'")
    
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(f"{ticker_symbol}.csv")
    blob.download_to_filename(f"data/{ticker_symbol}.csv")
    blob = bucket.blob(f"{ticker_symbol}.txt")
    blob.download_to_filename(f"data/{ticker_symbol}.txt")

    print(f"File downloaded from bucket '{bucket_name}' to 'data/{ticker_symbol}.csv and data/{ticker_symbol}.txt'.")

def upload_data(ticker_symbol, key_path="service_account_credentials.json"):
    """
    Uploads the updated CSV file to Google Cloud Storage.

    Parameters:
        ticker_symbol (str): The symbol of the financial instrument for which to upload the data.

    Returns:
        str: A message confirming the successful upload.
    """
    storage_client = storage.Client.from_service_account_json(key_path)
    load_dotenv()
    bucket_name = os.getenv('GOOGLE_CLOUD_BUCKET_NAME')
    if not bucket_name:
        raise ValueError("Bucket name is not set in the environment variable 'GOOGLE_CLOUD_BUCKET_NAME'")
    
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(f"{ticker_symbol}.csv")
    blob.upload_from_filename(f'data/{ticker_symbol}.csv')
    blob = bucket.blob(f"{ticker_symbol}.txt")
    blob.upload_from_filename(f'data/{ticker_symbol}.txt')

    return f"Data for {ticker_symbol} merged and uploaded to Cloud Storage."

def upload_txt_data(ticker_symbol, key_path="service_account_credentials.json"):
    storage_client = storage.Client.from_service_account_json(key_path)
    load_dotenv()
    bucket_name = os.getenv('GOOGLE_CLOUD_BUCKET_NAME')
    if not bucket_name:
        raise ValueError("Bucket name is not set in the environment variable 'GOOGLE_CLOUD_BUCKET_NAME'")
    
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(f"{ticker_symbol}.txt")
    blob.upload_from_filename(f'data/{ticker_symbol}.txt')

    return f"Text file for {ticker_symbol} updated and uploaded to Cloud Storage."
