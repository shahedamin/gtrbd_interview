

import yfinance as yf

class Trading_strategy:
    def __init__(self,symbol,from_date,to_date):
       self.company_name = symbol
       self.from_date = from_date
       self.to_date = to_date

    #Get data
    def data_acquisition(self):
        data = yf.Ticker(self.company_name)
        return data.history(start=self.from_date, end= self.to_date) # for see the data till today, use end = None

    # clean data
    def clean_data(self,data):
        remove_duplicate = data.drop_duplicates() # remove duplicates
        data = remove_duplicate.hist.ffill() # forward fill NaN values
        return data

    # Calculate the moving average
    def moving_average(self,data, window1=50, window2=200):
        ma_of_50 = data['Close'].rolling(window=window1).mean()
        ma_of_200 = data['Close'].rolling(window=window1).mean()
        return ma_of_50,ma_of_200

