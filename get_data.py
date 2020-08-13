import sys
from yahoo_finance_api2 import share
from yahoo_finance_api2.exceptions import YahooFinanceError
import pandas as pd
import numpy as np

stocks = ['ITSA4.SA', 'BBAS3.SA', 'BBDC4.SA', 'ITUB4.SA', 'PETR4.SA', 'GGBR4.SA', 'ABEV3.SA', 'CIEL3.SA', 'WEGE3.SA', 'BRFS3.SA', 'VALE3.SA', 'USIM5.SA', 'CSNA3.SA', 'GOAU4.SA', 'CMIG4.SA', 'ELET11.SA', 'FNOR11.SA', 'JBSS3.SA', 'LREN3.SA', 'IRBR3.SA', 'MTRE3.SA', 'POMO4.SA', 'B3SA3.SA', 'COGN3.SA', 'VVAR3.SA', 'TCSA3.SA', 'BPAN4.SA', 'USIM5.SA', 'USIM3.SA', 'SAPR4.SA', 'BPAC11.SA', 'ABCB4.SA',
'CMIG4.SA', 'CMIG3.SA', 'BRKM3.SA', 'SBSP3.SA', 'BRSR6.SA', 'SCAR3.SA', 'TEKA3.SA', 'PTNT3.SA', 'CTSA4.SA', 'PEAB3.SA']
times = ['5m', '1h']

for time in times:
    if time == '5m':
        days = 60
        frequency = 5
        type_frequency = share.FREQUENCY_TYPE_MINUTE
    else:
        days = 730
        frequency = 1
        type_frequency = share.FREQUENCY_TYPE_HOUR
    for stock in stocks:
        my_share = share.Share(stock)
        symbol_data = None

        try:
            symbol_data = my_share.get_historical(share.PERIOD_TYPE_DAY, days, type_frequency, frequency)
            
        except YahooFinanceError as e:
            print(e.message)
            sys.exit(1)


        df = pd.DataFrame(symbol_data)

        df.to_json('{}({}).json'.format(stock, time))

