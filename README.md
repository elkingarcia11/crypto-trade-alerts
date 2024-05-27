# Crypto Trade Alerts

The Crypto Trade Alerts project is a utility tool designed to provide trading alerts for cryptocurrency pairs based on various indicators and strategies. It offers functionalities for fetching, analyzing, and processing financial data, making trading decisions, and posting alerts on Twitter.

## Table of Contents

1. [Dependencies](#dependencies)
2. [Alert Module](#alert-module)
3. [Cryptocurrency Data Utils Module](#cryptocurrency-data-utils-module)
4. [Cloud Utils Module](#cloud-utils-module)
5. [CSV Utils Module](#csv-utils-module)
6. [Data Utils Module](#data-utils-module)
7. [Financial Utils Module](#financial-utils-module)
8. [Trading Utils Module](#trading-utils-module)
9. [Twitter Utils Module](#twitter-utils-module)
10. [Twitter Link](#twitter-link)

## Dependencies

Located in the requirements.txt file:

- google.cloud
- pandas
- pytz
- requests
- tweepy

Make sure these packages are installed and accessible in your Python environment before using the `alert` function.

## Alert Module

The `alert` function is a utility function designed to provide trading alerts based on various indicators and strategies. It utilizes several modules for fetching and analyzing financial data, making trading decisions, and posting alerts on Twitter.

### Usage

```python
alert("AAPL")
```

This will trigger the alert function for the AAPL (Apple Inc.) stock symbol.

## Cryptocurrency Data Utils Module

The `crypto_data_utils` module provides functions for fetching and processing cryptocurrency data.

## Cloud Utils Module

The `cloud_utils` module offers functions for interaction with Google Cloud Storage to facilitate the fetching and uploading of financial data.

Prior to utilizing these functions, ensure that the GOOGLE_CLOUD_BUCKET_NAME environment variable is set with the name of the Google Cloud Storage bucket.

**Note**: You need a `service_account_credentials.json` file to configure the connection to the Cloud Storage bucket.

## CSV Utils Module

The `csv_utils` module offers functions for working with CSV files containing financial data.

## Data Utils Module

The `data_utils` module provides functions for formatting financial data into a more readable format.

## Financial Utils Module

The `financial_utils` module offers functions for calculating financial indicators and generating indicators for financial data.

## Trading Utils Module

The `trading_utils` module provides functions for implementing trading strategies and making trading decisions.

## Twitter Utils Module

The `twitter_utils` module provides functions for interacting with the Twitter API to post tweets.

## Twitter Link

Users can easily find and [follow us on Twitter for real-time alerts!](https://x.com/TheBitcoinAlert)





