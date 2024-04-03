
import yfinance as yf

class Trading_strategy:
    def __init__(self,symbol,from_date,to_date):
       self.company_name = symbol
       self.from_date = from_date
       self.to_date = to_date

    def data_acquisition(self):

        aapl = yf.Ticker(self.company_name)
        hist = aapl.history(start=self.from_date, end= self.to_date) # for see the data till today, use end = None
        print(hist)

      
aapl_strategy=Trading_strategy("AAPL","2024-02-01","2024-04-01")
aapl_strategy.data_acquisition()
