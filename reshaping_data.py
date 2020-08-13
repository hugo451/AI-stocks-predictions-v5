import numpy as np
import pandas as pd


stocks = ['ITSA4.SA', 'BBAS3.SA', 'BBDC4.SA', 'ITUB4.SA', 'PETR4.SA', 'GGBR4.SA', 'ABEV3.SA', 'CIEL3.SA', 'WEGE3.SA', 'BRFS3.SA', 'VALE3.SA', 'USIM5.SA', 'CSNA3.SA', 'GOAU4.SA', 'CMIG4.SA', 'ELET11.SA', 'FNOR11.SA', 'JBSS3.SA', 'LREN3.SA', 'IRBR3.SA', 'MTRE3.SA', 'POMO4.SA', 'B3SA3.SA', 'COGN3.SA', 'VVAR3.SA', 'TCSA3.SA', 'BPAN4.SA', 'USIM5.SA', 'USIM3.SA', 'SAPR4.SA', 'BPAC11.SA', 'ABCB4.SA',
'CMIG4.SA', 'CMIG3.SA', 'BRKM3.SA', 'SBSP3.SA', 'BRSR6.SA', 'SCAR3.SA', 'TEKA3.SA', 'PTNT3.SA', 'CTSA4.SA', 'PEAB3.SA']

times = ['5m', '1h']

for time in times:
    df = pd.DataFrame()
    for stock in stocks:

        data = pd.read_json('{}({}).json'.format(stock, time))

        data = data.filter(['close', 'high', 'low', 'volume'])

        data = data.dropna()

        dataset = data.values
        data_len = len(dataset)


        x_train = []
        y_train = []

        for i in range(60, data_len):
            x_train.append(np.array(dataset[i-60:i, :]))
            if (dataset[i, 0] - dataset[i-1, 0]) > 0:
                y_train.append(np.array([[1]]))
            else:
                y_train.append(np.array([[0]]))


        d = {'X_TRAIN' : x_train, 'Y_TRAIN' : y_train}


        dataframe = pd.DataFrame(d)
        df = df.append(dataframe, ignore_index=True)

    print(df.index[-1])
    df.to_json('data({}).json'.format(time))