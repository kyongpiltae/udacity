import pandas as pd
import matplotlib.pyplot as plt

def get_mean_volume(symbol):
    df = pd.read_csv("data/{}.csv".format(symbol))
    return df['Volume'].mean()


def test_run():
    df = pd.read_csv("data/AAPL.csv")
    print df['Adj Close']
    df['Adj Close'].plot()
    plt.show()
    
def test_run1():
    for symbol in ['AAPL','IBM']:
        print "mean Volume"
        print symbol, get_mean_volume(symbol)

if __name__ == "__main__":
    test_run()
