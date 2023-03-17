import pandas as pd
import datetime
from datetime import timedelta

file=pd.read_csv('input.csv',encoding='utf-8')
df=pd.DataFrame(file)
df = df.replace('\n','', regex=True)


for i in range (len(df.index)):
    df['Date'].str.replace('T',' ')
    if(df['Body'].str.contains('χθες|Χθες').iloc[i]):


    

        new_date_string = df['Date'].str[:-5].str.replace('T',' ').iloc[i]
        datetime_object = datetime.datetime.strptime(new_date_string,'%Y-%m-%d %H:%M:%S')
        #print(datetime_object)
        test=datetime_object + datetime.timedelta(days=-1)
        df['Date'].iloc[i]=test.strftime("%Y-%m-%dΤ%H:%M:%S+0300")


    elif (df['Body'].str.contains('αύριο|Αύριο').iloc[i]):
        new_date_string = df['Date'].str[:-5].str.replace('T',' ').iloc[i]
        datetime_object = datetime.datetime.strptime(new_date_string,'%Y-%m-%d %H:%M:%S')
        #print(datetime_object)
        test=datetime_object + datetime.timedelta(days=+1)
        df['Date'].iloc[i]=test.strftime("%Y-%m-%dΤ%H:%M:%S+0300")

#print(df['Date'][:12])
print(df.shape)

'''

for i in range(len(df.index)):
#indexAge = df[(df['Date'] >'2024')].index #& (df['Date'] <= '2023') ].index
    if (df['Date'].str.contains('\+0300',regex=True).iloc[i]):
        df['Date'] = pd.to_datetime(df['Date'],format="%Y-%m-%dT%H:%M:%S+0300")
    elif (df['Date'].str.contains('\+0200',regex=True).iloc[i]):
        df['Date'] = pd.to_datetime(df['Date'],format="%Y-%m-%dΤ%H:%M:%S+0200")

    res = df[~(df['Date'] >= '2018-12-01')] & df[~(df['Date']<='2022-06-19')]
print(res.shape)
'''

df['Date2']=df['Date'].str[0:19].str.replace('T',' ').str.replace('Τ',' ')
print(df['Date2'])

df.drop(df.index[89], inplace=True)

    

df['Date2'] = pd.to_datetime(df['Date2'],format='%Y-%m-%d %H:%M:%S')
print(df.shape)


a = df['Date2'] >= '2018-12-01'
b = df['Date2'] <= '2022-06-20'
df = df[a & b]
del df['Date']
print(df[:20])
print(df.shape)
df.to_csv('final.csv')
