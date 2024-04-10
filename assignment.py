''' How this code works -  First, initiate the aaple object, get the historical data, clean the data, find the moving averages, determine golden or death cross. Based on the cross , we will take the buying decision. For taking buying decision- First check the cross. If golden cross found cosecutively, we will find out the index among all golden crosses before encounter the death cross, from where we can buy highest share amount. We will count this index as the buying position. when death cross will encounter we will close the position and take profit. This will be profit from one trade. We will store this profit value into a list. When traversing the whole historical data, maybe we will find another trade opportunity. If find another opportunity , will take profit as previous trade . When we will finish the traversing of whole data, now we will add all the profit or losses together and will find the final profit / loss '''


import yfinance as yf
import pandas as pd

class Trading_strategy:
    def __init__(self,symbol,from_date,to_date):
       self.company_name = symbol
       self.from_date = from_date
       self.to_date = to_date

    # Get stock historical data
    def data_acquisition(self):
        data = yf.Ticker(self.company_name).history(start=self.from_date, end= self.to_date) # for see the data till today, use end = None
        return data

    # clean data
    def clean_data(self,data):
        remove_duplicate = data.drop_duplicates() # remove duplicates
        data = remove_duplicate.ffill() # forward fill NaN values
        return data

    # Calculate the moving average
    def moving_average(self,data, window1=50, window2=200):
        ma_of_50 = data['Close'].rolling(window=window1).mean()
        ma_of_200 = data['Close'].rolling(window=window2).mean()
        return ma_of_50,ma_of_200

    
    def cross_determination(self, short_term_ma, long_term_ma):
        crosses = pd.Series(index=short_term_ma.index, dtype='object')  # Create an empty Series with the same index as short_term_ma
    
        # Determine cross for each value
        for date, short_ma_value in short_term_ma.items():
            long_ma_value = long_term_ma.loc[date]
            if short_ma_value > long_ma_value:
                crosses[date] = 'Golden Cross'
            else:
                crosses[date] = 'Death Cross'
        
        return crosses


    def take_Buying_position(self, crosses, budget=5000):
        maximum_quantity_of_shares_to_purchase = 0  # Initialize max quantity
        position_taken = False  # Initialize position_taken flag
        profit_losses_in_every_position = []
        final_profit_losses = 0

        for idx, (date, cross) in enumerate(crosses.items()):   # add idx and enumerate

            # Get stock price for that index
            stock_price = data['Close'].loc[date]

            if cross == 'Golden Cross':
                quantity_will_get = budget / stock_price
                if quantity_will_get >  maximum_quantity_of_shares_to_purchase :
                    maximum_quantity_of_shares_to_purchase  = quantity_will_get
                    buying_amount =  maximum_quantity_of_shares_to_purchase  * stock_price
                    position_taken = True

            else:
                if position_taken:  # Check if position is already taken
                    selling_amount =  maximum_quantity_of_shares_to_purchase  * stock_price
                    profit = selling_amount - buying_amount
                    maximum_quantity_of_shares_to_purchase  = 0
                    position_taken = False
                    profit_losses_in_every_position.append(profit)

            if idx == len(crosses)-1 and position_taken == True :  # check if in last loop
                selling_amount =  maximum_quantity_of_shares_to_purchase  * stock_price
                profit = selling_amount - buying_amount
                maximum_quantity_of_shares_to_purchase  = 0
                position_taken = False
                profit_losses_in_every_position.append(profit)

        for i in profit_losses_in_every_position:
            final_profit_losses += i

        if final_profit_losses > 0:
            print('Profit:', final_profit_losses)
        elif final_profit_losses == 0:
            print('No Profit / Loss')
        else:
            print('Loss:', final_profit_losses)


aapl = Trading_strategy("AAPL", "2020-03-01", "2022-10-11")
data = aapl.data_acquisition()
cleaned_data = aapl.clean_data(data)
short_term_ma, long_term_ma = aapl.moving_average(cleaned_data)
crossover = aapl.cross_determination(short_term_ma, long_term_ma)
aapl.take_Buying_position(crossover)