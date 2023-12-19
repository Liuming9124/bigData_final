import mplfinance as mpf

import pandas as pd
daily = pd.read_csv('./reversed_file.csv',index_col=0,parse_dates=True)
daily.index.name = 'Date'
print(daily.shape)

# mpf.plot(daily)

# K線圖
# mpf.plot(daily,type='candle')

# k chart with moving average
# mpf.plot(daily,type='candle',mav=(3,6,9))

# mpf.plot(daily,type='candle',mav=(3,6,9),volume=True)

mpf.plot(daily,type='candle',mav=(3,6,9),volume=True,show_nontrading=True)
