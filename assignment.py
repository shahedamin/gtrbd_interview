
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
        hist = aapl.history(period="1mo")
        print(hist)

      
aapl_strategy=Trading_strategy("AAPL")
aapl_strategy.data_acquisition()

# import yfinance as yf


# # get historical market data
# hist = yf.Ticker("AAPL").history(period="5d")
# print(hist)

