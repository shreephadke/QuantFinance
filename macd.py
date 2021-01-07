def macd():
    # MACD formula
    macd = EMA(12_days) - EMA(26_days)
    # extract signal_line pricing data, which is really just the EMA for the last 9 days
    signal_line = EMA(9_days)
    # the signal line is plotted along with the MACD graph and compared

    # if the MACD crosses the signal line and rises above it, it functions as a buy trigger
    if (macd > signal_line):
        buy(SQQQ)
    # else, if the MACD crosses the signal line and falls below it, it functions as a sell trigger
    else:
        sell(SQQQ)
    
