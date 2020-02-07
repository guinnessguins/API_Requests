import requests
from datetime import datetime
import json
import pickle
import pandas as pd
from pandas.io.json import json_normalize
from datetime import datetime
import time
from datetime import timedelta
starttime=time.time()
while True:
        reskey_info=requests.get('http://www.coinwarz.com/v1/api/apikeyinfo?apikey=2fa117046a394237b3c5a08238297fbd')
        res=requests.get('http://www.coinwarz.com/v1/api/profitability?apikey=2fa117046a394237b3c5a08238297fbd&algo=all', params='ToUSD')
        #rescoininfo_=requests.get('http://www.coinwarz.com/v1/api/coininformation/?apikey=2fa117046a394237b3c5a08238297fbd&cointag=all')
        keyinfo_js=reskey_info.json()
        #coininfo_js=rescoininfo.json()
        json_df=res.json()
        ddf=json_df['Data']
        date=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        date={'Date': date}
        keyinfo_js.update(date)
        from pandas.io.json import json_normalize
        info_pd = pd.DataFrame.from_dict(json_normalize(keyinfo_js), orient='columns')
        info_pd_csv=info_pd.to_csv(index=True, mode= 'a', header=False)
        filename="/home/pedro/Downloads/190626_info_n_High_Day.csv"
        with open(filename, 'a') as fp:
                fp.write(info_pd_csv)
                #print(ddf)
        print(keyinfo_js)
        from pandas.io.json import json_normalize
        pd_df = pd.DataFrame.from_dict(json_normalize(ddf), orient='columns')
        var1=['Algorithm', 'AvgProfitRatio', 'BlockCount', 'BlockReward', 'BlockTimeInSeconds', 'CoinName' , 'CoinTag']
        var2=['CoinTag', 'Difficulty', 'Exchange', 'ExchangeRate', 'ExchangeVolume', 'HealthStatus']
        var3=['CoinTag','IsBlockExplorerOnline', 'IsExchangeOnline', 'Message', 'ProfitRatio']
        pd_df['idx'] = 1
        pd_df_wide1 = pd_df.pivot(index='idx', columns='CoinTag', values = var1)
        pd_df_wide2 = pd_df.pivot(index='idx', columns='CoinTag', values = var2)
        pd_df_wide3 = pd_df.pivot(index='idx', columns='CoinTag', values = var3)
        pd_df_wide1.columns = [''.join(col).strip() for col in pd_df_wide1.columns.values]
        pd_df_wide2.columns = [''.join(col).strip() for col in pd_df_wide2.columns.values]
        pd_df_wide3.columns = [''.join(col).strip() for col in pd_df_wide3.columns.values]
        pd_df1_csv=pd_df_wide1.to_csv(index=True, mode='a', header=False)
        pd_df2_csv=pd_df_wide2.to_csv(index=True, mode='a', header=False)
        pd_df3_csv=pd_df_wide3.to_csv(index=True, mode='a', header=False)
        with open("/home/pedro/Downloads/190626_mining_1_High_Day.csv",'a') as mining:
                mining.write(pd_df1_csv)
        with open("/home/pedro/Downloads/190626_mining_2_High_Day.csv",'a') as mining2:
                mining2.write(pd_df2_csv)
        with open("/home/pedro/Downloads/190626_mining_3_High_Day.csv",'a') as mining3:
                mining3.write(pd_df3_csv)
        time.sleep(360.0 - ((time.time() - starttime) % 360.0))

                
 







