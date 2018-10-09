"""Utility functions"""

import os
import pandas as pd

def symbol_to_path(symbol, base_dir="data"):
    """Return CSV file path given ticker symbol."""
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))


def get_data(symbols, dates):
    """Read stock data (adjusted close) for given symbols from CSV files."""
    df = pd.DataFrame(index=dates)
    if 'SPY' not in symbols:  # add SPY for reference, if absent
        symbols.insert(0, 'SPY')

    for symbol in symbols:
        # TODO: Read and join data for each symbol
        target = symbol_to_path(symbol)
        df_temp = pd.read_csv(target,index_col="Date",parse_dates=True,usecols=['Date','Adj Close'],na_values=['NaN'])
        df_temp = df_temp.rename(columns = {'Adj Close': symbol})
        df = df.join(df_temp,how='inner')
    
    df.dropna()

    return df


def test_run():
    # Define a date range
    dates = pd.date_range('2010-01-01', '2010-12-31')

    # Choose stock symbols to read
    symbols = ['GOOG', 'IBM', 'GLD']
    
    # Get stock data
    df = get_data(symbols, dates)
    df1=df.ix['2010-01-01':'2010-01-10']
    print df1[['GOOG',"GLD"]]
    df1.plot()
    


if __name__ == "__main__":
    test_run()
