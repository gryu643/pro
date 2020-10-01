from backtesting import Strategy
from backtesting.lib import crossover
import pandas as pd
from backtesting import Backtest


def SMA(values, n):
    """
    Return simple moving average of `values`, at
    each step taking into account `n` previous values.
    """
    return pd.Series(values).rolling(n).mean()


class SmaCross(Strategy):
    # Define the two MA lags as *class variables*
    # for later optimization
    n1 = 10
    n2 = 20

    def init(self):
        # Precompute the two moving averages
        self.sma1 = self.I(SMA, self.data.Close, self.n1)
        self.sma2 = self.I(SMA, self.data.Close, self.n2)

    def next(self):
        # If sma1 crosses above sma2, close any existing
        # short trades, and buy the asset
        if crossover(self.sma1, self.sma2):
            self.position.close()
            self.buy()

        # Else, if sma1 crosses below sma2, close any existing
        # long trades, and sell the asset
        elif crossover(self.sma2, self.sma1):
            self.position.close()
            self.sell()


def main():
    # データの読み込み
    usecols = ['time', 'close', 'open', 'high', 'low']
    df = pd.read_csv("usd_10min_api.csv", usecols=usecols,
                     index_col='time', parse_dates=True)

    # カラム名の頭文字は大文字でなくてはならない
    df.columns = ['Close', 'Open', 'High', 'Low']

    bt = Backtest(df, SmaCross, cash=100000, commission=0.005)

    output = bt.run()

    print(output)

    stats = bt.optimize(n1=range(5, 30, 5),
                        n2=range(10, 100, 5),
                        maximize='Equity Final [$]',
                        constraint=lambda param: param.n1 < param.n2)

    print(stats)


if __name__ == '__main__':
    main()
