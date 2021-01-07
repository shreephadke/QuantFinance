# Upper bound: SMA + D * sqrt((sum(y_j - MA)^2))/n)
# Lower bound: SMA - D * sqrt((sum(y_j - MA)^2))/n)

import math

def bollinger_bands():

    # 20-day bollinger band calculation
    N = 20

    # scrapes historical price data over last 20 days
    hist = []

    # call SMA function to calculate the 20 day simple moving average using historical price data
    sma = SMA(hist)

    # coefficient that denotes how many standard deviations above or below the band is
    # upper band: 2 std. devs. above the EMA
    # middle band: 0 std. devs. away from EMA (middle band is the EMA)
    # lower band: 2 std. devs. below the EMA
    D = 2

    # calculate summation of the residual square between the current price and SMA for the 20 days
    sum = 0
    for i in range(N):
        sum += (current_price - sma) * (current_price - sma)

    std_dev = sqrt(sum/N)

    # upper bound and lower bound formulas (refer to comments at top)
    upper_bound = sma + D*std_dev
    lower_bound = sma - D*std_dev

    # if price is near lower band, sell
    if (current_price <= lower_bound + lower_bound*0.05)
        sell(stock)

    # if price is near upper band, buy
    if (current_price >= upper_bound - upper_bound*0.05)
        buy(stock)
