import pandas as pd

def test_run():
    start_date='2010-01-22'
    end_date = '2010-01-26'
    dates = pd.date_range(start_date,end_date)
    print dates[0]

    df1 = pd.DataFrame(index=dates)
    print df1.head()

    dfSPY = pd.read_csv("data/SPY.csv",index_col="Date",parse_dates=True,usecols=['Date','Adj Close'],na_values=['NaN'])
    print dfSPY.head()


    df1= df1.join(dfSPY,how="inner")
    print df1.head()
    df1.dropna()
    print df1

if __name__ == "__main__":
    test_run()