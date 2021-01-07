import talib
 
 
# Setup our variables
def initialize(context):
    context.stocks = symbols('SQQQ')
    context.target_pct_per_stock = 1.0 / len(context.stocks)
    context.LOW_RSI = 30
    context.HIGH_RSI = 70
    
    schedule_function(rebalance, date_rules.every_day(), time_rules.market_open())
 
# Rebalance daily.
def rebalance(context, data):
    
    # Load historical data for the stocks
    prices = data.history(context.stocks, 'price', 20, '1d')
    close_history = data.history(context.stocks, 'price', 30, '1d')
    curr = data.current(context.stocks, 'price')
    close = close_history.mean()
    
    rsis = {}
    
    # Loop through our list of stocks
    for stock in context.stocks:
        # Get the rsi of this stock.
        rsi = talib.RSI(prices[stock], timeperiod=14)[-1]
        rsis[stock] = rsi
        current = curr[stock]
        closes = close[stock]
        
        current_position = context.portfolio.positions[stock].amount
        
        # RSI is above 70 and we own shares, time to sell
        if rsi > context.HIGH_RSI and current_position > 0 and data.can_trade(stock):
            order_target(stock, 0)
            print(rsi)
   
        # RSI is below 30 and we don't have any shares, time to buy
        elif rsi < context.LOW_RSI and current_position == 0 and data.can_trade(stock):
            order_target_percent(stock, 1)
            print(rsi)
            
        if current > closes and data.can_trade(stock) and current_position == 0:
            order_target_percent(stock,1)
            print(rsi)
            
            
        
            
    