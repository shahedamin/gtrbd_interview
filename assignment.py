
import yfinance as yf


class Trading_strategy:
    # def __init__(self,symbol,from_date,to_date):
    def __init__(self,symbol):
       self.company_name = symbol
    #    self.from_date = from_date
    #    self.to_date = to_date

    def data_acquisition(self):
        aapl = yf.Ticker(self.company_name)

        # get historical market data
        hist = aapl.history(start="2024-01-04", end=None)
        print(hist)

      
aapl_strategy=Trading_strategy("AAPL")
aapl_strategy.data_acquisition()
