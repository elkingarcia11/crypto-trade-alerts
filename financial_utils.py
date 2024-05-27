import pandas as pd

def vwap(data):
    """
    Calculates the Volume Weighted Average Price (VWAP) for the given financial data.

    Parameters:
        data (pandas.DataFrame): The financial data containing 'Close' prices and 'Volume'.

    Returns:
        pandas.DataFrame: The input DataFrame with an additional column 'VWAP' containing VWAP values.
    """
    close_prices = data['Close']
    volume = data['Volume']
    vwap_period = 20
    cumulative_price_volume = (close_prices * volume).rolling(window=vwap_period).sum()
    cumulative_volume = volume.rolling(window=vwap_period).sum()
    vwap = cumulative_price_volume / cumulative_volume
    data['VWAP'] = vwap  # Assign VWAP values back to DataFrame
    return data

def generate_vwap_indicator(ticker_symbol):
    """
    Generates the Volume Weighted Average Price (VWAP) indicator for the given financial instrument's data.

    Parameters:
        ticker_symbol (str): The symbol of the financial instrument.

    Returns:
        None
    """
    data = pd.read_csv(f'data/{ticker_symbol}.csv')
    data = vwap(data)
    data.to_csv(f'data/{ticker_symbol}_WITH_INDICATORS.csv', mode='w', index=False)
