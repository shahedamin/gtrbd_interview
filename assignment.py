
import yfinance as yf

class Trading_strategy:
    def __init__(self,symbol,from_date,to_date):
       self.company_name = symbol
       self.from_date = from_date
       self.to_date = to_date

    #Get data
    def data_acquisition(self):
        aapl = yf.Ticker(self.company_name)
        self.hist = aapl.history(start=self.from_date, end= self.to_date) # for see the data till today, use end = None

    # clean data
    def clean_data(self):
        self.hist = self.hist.drop_duplicates() # remove duplicates
        self.hist = self.hist.ffill() # forward fill NaN values

      
aapl_strategy=Trading_strategy("AAPL","2024-02-01",None)
aapl_strategy. data_acquisition()
aapl_strategy.clean_data()
print (aapl_strategy.hist)

