import pandas as pd

df=pd.read_csv('thebest_lat_long.csv')

df.drop('Unnamed: 0', inplace=True, axis=1)
df.drop('Unnamed: 0.1', inplace=True, axis=1)
df.to_csv('thebest_lat_long_2.csv',index=False)

df['keyword'] = 0

# assign a value of 1 to the first 10 rows
df.iloc[:20, df.columns.get_loc('keyword')] = 'πλήθος_κόσμου'

# assign a value of 2 to the next 10 rows
df.iloc[20:60, df.columns.get_loc('keyword')] = 'πυρκαγιά_φωτιά'
df.iloc[60:107, df.columns.get_loc('keyword')] = 'τροχαίο'
df.iloc[107:140, df.columns.get_loc('keyword')] = 'γήπεδο'
df.iloc[140:193, df.columns.get_loc('keyword')] = 'Προμηθέας_μπάσκετ'
df.iloc[194:215, df.columns.get_loc('keyword')] = 'αγώνας'
df.iloc[215:242, df.columns.get_loc('keyword')] = 'ατμόσφαιρα'
df.iloc[243:278, df.columns.get_loc('keyword')] = 'πορεία_απεργία'
df.iloc[278:310, df.columns.get_loc('keyword')] = 'ρύπανση'
df.iloc[310:, df.columns.get_loc('keyword')] = 'κυκλοφορία_κορονοιός_απαγόρευση'
df.iloc[359:363,df.columns.get_loc('keyword')] = 'μικροσωματίδια'
print(df.columns)
df.to_csv('thebest_lat_long_keywords.csv',index=False)