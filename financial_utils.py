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

def update_vwap(ticker_symbol):
    """
    Updates the Volume Weighted Average Price (VWAP) for the given financial data,
    ensuring it uses original 20-day rolling periods for calculation.

    Parameters:
        ticker_symbol (str): The ticker symbol of the stock.
        new_data (pandas.DataFrame): The new financial data to be added containing 'Close' prices and 'Volume'.

    Returns:
        pandas.DataFrame: The updated DataFrame with the VWAP calculated.
    """
    
    # Load the existing data from the CSV file
    data = pd.read_csv(f'data/{ticker_symbol}.csv')
    
    # Define the period for VWAP calculation
    vwap_period = 20
    
    # Calculate cumulative price-volume and cumulative volume
    data['Cumulative_Price_Volume'] = (data['Close'] * data['Volume']).cumsum()
    data['Cumulative_Volume'] = data['Volume'].cumsum()
    
    # Calculate VWAP for the entire dataset
    data['VWAP'] = data['Cumulative_Price_Volume'] / data['Cumulative_Volume']
    
    # Correct VWAP for the rolling window
    for i in range(vwap_period, len(data)):
        data.at[i, 'VWAP'] = (
            (data['Cumulative_Price_Volume'].iat[i] - data['Cumulative_Price_Volume'].iat[i - vwap_period]) /
            (data['Cumulative_Volume'].iat[i] - data['Cumulative_Volume'].iat[i - vwap_period])
        )
    
    # Handle the initial period where VWAP cannot be calculated
    initial_vwap = (
        data['Cumulative_Price_Volume'].iloc[:vwap_period] / data['Cumulative_Volume'].iloc[:vwap_period]
    )
    data['VWAP'].iloc[:vwap_period] = initial_vwap
    
    # Drop the intermediate columns used for calculation
    data = data.drop(columns=['Cumulative_Price_Volume', 'Cumulative_Volume'])
    
    # Save the updated data back to the CSV file
    data.to_csv(f'data/{ticker_symbol}.csv', index=False)