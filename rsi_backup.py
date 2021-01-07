def initialize(context):
    # Reference to SQQQ stock.
    context.sqqq = sid(39211)

    schedule_function(rebalance, date_rules.every_day(), time_rules.market_close(minutes = 30))
    schedule_function(record_vars, date_rules.every_day(), time_rules.market_close())
    schedule_function(record_vars, date_rules.every_day(), time_rules.market_close())

    
def rebalance(context, data):
    # scrapes historical data for SQQQ stock over last 14 days in 1 day intervals
    hist = data.history(context.sqqq, 'close', 15, "1d")
    current_price = data.current(context.sqqq, 'price')
    # print(hist)
    gains = []
    losses = []
        
    # iterates over historical data list
    for i in range (len(hist) - 1):
        # if there is a positive change in price, add to gains list
        if hist[i+1] > hist[i]:
            gains.append(hist[i+1] - hist[i])
        # if there is a negative change in price, add to losses list
        else:
            losses.append(hist[i] - hist[i+1])
            
    average_gains = sum(gains)/len(hist)
    average_losses = sum(losses)/len(hist)
    # Relative Strength
    rs = average_gains/average_losses
    # RSI Formula
    rsi = 100-(100/(1+rs))
       
    
    if data.can_trade(context.sqqq):
        # if the RSI is equal to or above the Upperbound of 70, set portfolio to 100% SQQQ
        if (rsi >= 70):
            # only the first overbought RSI is relevant
            order_target_percent(context.sqqq, 0)
            print("Overbought, RSI: {}".format(rsi))
        elif (rsi <= 30):
            # only the first oversold RSI is relevant
            order_target_percent(context.sqqq, 1.0)
            print("Oversold, RSI: {}".format(rsi))
            
def record_vars(context, data):
    # scrapes historical data for SQQQ stock over last 14 days in 1 day intervals
    hist = data.history(context.sqqq, 'close', 15, "1d")
    # print(hist)
    gains = []
    losses = []
        
    current_price = data.current(context.sqqq, 'price')

    # iterates over historical data list
    for i in range (len(hist) - 1):
        # if there is a positive change in price, add to gains list
        if hist[i+1] > hist[i]:
            gains.append(hist[i+1] - hist[i])
        # if there is a negative change in price, add to losses list
        else:
            losses.append(hist[i] - hist[i+1])
            
    average_gains = sum(gains)/len(hist)
    average_losses = sum(losses)/len(hist)
    # Relative Strength
    rs = average_gains/average_losses
    # RSI Formula
    rsi = 100-(100/(1+rs))
    record(rsi = rsi, UB = 70, LB = 30)
    record(price = current_price)