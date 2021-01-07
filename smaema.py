#installing the alpaca api using !pip
!pip install alpaca-trade-api
#installing the mplfinance package using !pip
!pip install mplfinance
# Required modules and packages
import pandas as pd # We import financial data into a pandas Data Frame
import numpy as np
import matplotlib.pyplot as plt
import mplfinance as mpf

import pandas_datareader # Used to get data from different sources
import plotly.graph_objects as go

from pandas_datareader import data as wb # we use the 'data' module of the pandas_datareader package to get our data
# wb stands for web
# for example, to get the AAPL stock data from 2010 using Yahoo Finance
stockdata = wb.DataReader('AAPL', data_source='yahoo', start='2010-1-1',end = '2010-3-1')

#we now create another dataframe 'stockclosing' where we only store the closing values of the stock from 'stockdata'
stockclosing = stockdata['Close']

#the following function is in-built in pandas and allows us to compute simple moving average
#here, we compute the simple moving average of closing prices
#the 'window' allows us to determine the time period over which we want to compute the simple moving average. For eg. to compute the 10 day sma, we send in the argument "span = 10"
#the .rolling() function makes sure that the sma is computed on a rolling basis
sma = stockclosing.rolling(window = 10).mean()

#the following function is in-built in pandas and allows us to compute the exponential moving average
#here, we compute the exponential moving average of the closing prices
#the 'span' allows us to determine the number of days for which we wish to compute the ema. For eg. to compute the 10 day ema we write "span = 10"
#adjust = false makes sure that the ema is calculated on a recurring basis
ema = stockclosing.ewm(span=20,adjust=False,).mean()

mpf.plot(stockdata, type='candle', style='charles',
       title='Apple , Jan - 2010',
       ylabel='Price ($)',
       ylabel_lower='volume',
       volume=True,
       mav=(3,6,9))

#plt.figure lets us adjust the size of the graph
#the format of the function is plt.figure(figsize =[enter width in inches,enter height in inches])
plt.figure(figsize=[10,5])


#to plot what we have computed, we use the matplotlib.pyplot module and the arguments it takes are what we want to plot and the label
plt.plot(ema,label='EMA 20')
plt.plot(sma,label = 'SMA 10')

plt.legend(loc = 'upper right') #the argument for the legend() function lets us decide where we want to display the legend on the figure

mpf.plot(
           stockdata,
           type='candle',
           style='charles',
           title='Apple, Jan - 2010',
           ylabel='Price ($)')
#the mpf.plot() function allows us to plot candlesticks with the following as argument
mpf.plot(stockdata, #this is the dataframe which we want to plot in the form of candlesticks
        type='candle', #setting the plot type to 'candle' to plot candlestick data
        style='charles', #we choose the style of candlesticks. the 'charles' style plots each candlestick in either green or red
       title='Apple, Jan - 2010', #this is the title of the candlestick data chart that will be displayed
       ylabel='Price ($)', #the labbel of the y axis
       ylabel_lower='Volume of Stock traded', #the label of the lower part of the y axis(Only needed if we are plotting volume)
       volume=True, #whether or not display the amount of stock bough tor sold
       mav=(10)#to plot the 10 day simple moving average
       )
