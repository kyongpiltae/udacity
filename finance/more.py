import pandas as pd

def test_run():
    start_date='2010-01-22'
    end_date = '2010-01-26'
    dates = pd.date_range(start_date,end_date)
    print dates[0]


    df1 = pd.DataFrame(index=dates)

    dfSPY = pd.read_csv("data/SPY.csv",index_col="Date",parse_dates=True,usecols=['Date','Adj Close'],na_values=['NaN'])
    dfSPY= dfSPY.rename(columns={'Adj Close':'SPY'})


    df1= df1.join(dfSPY,how="inner")

    symbols = ["GOOG",'IBM','GLD']
    for symbol in symbols:
        df_temp = pd.read_csv("data/{}.csv".format(symbol),index_col="Date",parse_dates=True,usecols=['Date','Adj Close'],na_values=['NaN'])
        df_temp = df_temp.rename(columns = {'Adj Close': symbol})
        df1=df1.join(df_temp)
   
    print df1

if __name__ == "__main__":
    test_run()