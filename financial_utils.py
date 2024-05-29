import pandas as pd
import numpy as np
def generate_vwap(ticker_symbol):
    """
    Calculates the Volume Weighted Average Price (VWAP) for the given financial data.

    Parameters:
        data (pandas.DataFrame): The financial data containing 'Close' prices and 'Volume'.

    Returns:
        pandas.DataFrame: The input DataFrame with an additional column 'VWAP' containing VWAP values.
    """
    # Load the data from the CSV file
    data = pd.read_csv(f'data/{ticker_symbol}.csv')
    
    close_prices = data['Close']
    volume = data['Volume']
    vwap_period = 20
    cumulative_price_volume = (close_prices * volume).rolling(window=vwap_period).sum()
    cumulative_volume = volume.rolling(window=vwap_period).sum()
    vwap = cumulative_price_volume / cumulative_volume
    data['VWAP'] = vwap  # Assign VWAP values back to DataFrame
    
    data.to_csv(f'data/{ticker_symbol}.csv', mode='w', index=False)
    print("VWAP generated for data")