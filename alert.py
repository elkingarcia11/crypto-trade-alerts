import cloud_utils
import crypto_data_utils
import financial_utils
import trading_utils
import twitter_utils
from datetime import datetime, timezone

def alert(ticker_symbol):
    """
    Generates a trading alert for the given ticker symbol based on the VWAP strategy.

    The function performs the following steps:
    1. Fetches the latest data from the cloud.
    2. Merges the latest data with existing data.
    3. Uploads the updated data back to the cloud.
    4. Calculates new financial indicators (VWAP in this case).
    5. Determines a trading decision (buy, sell, hold) based on the VWAP strategy.
    6. Posts the trading decision on Twitter if a decision is made.

    Parameters:
        ticker_symbol (str): The ticker symbol of the cryptocurrency (e.g., "BTC").

    Returns:
        None
    """

    # Fetch data from cloud (commented out as per the original code)
    cloud_utils.fetch_data(ticker_symbol)

    # Fetch and merge latest data
    crypto_data_utils.fetch_and_save_latest_data(ticker_symbol)

    # Push data to cloud (commented out as per the original code)
    cloud_utils.upload_data(ticker_symbol)

    # Calculate new indicators (VWAP in this case)
    financial_utils.generate_vwap(ticker_symbol)

    # Determine if should buy, sell, or hold
    decision = trading_utils.published_vwap_strategy(ticker_symbol)

    # Get the current date and time in UTC
    utc_now = datetime.now(timezone.utc)
    utc_now = utc_now.strftime('%Y-%m-%d %H:00')

    # Print the current date and time in UTC
    print("Current date and time in UTC:", utc_now)

    if decision:
        decision = f"{utc_now}: " + decision
        # Tweet decision
        twitter_utils.tweet(decision)


# Example usage
alert("BTC")
