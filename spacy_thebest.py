import spacy
import datefinder
import re
import json
from sutime import SUTime
from datetime import datetime
from datetime import timedelta
import pandas as pd
import datetime
'''
#text to datetime, and then if text = yesterday or text = tomorrow then timedelta (day=1 or -1)
date_string = "2022-09-16T22:42:01+0300"
print(len(date_string))

new_date_string = date_string[:-5].replace('T',' ')
print(new_date_string)
datetime_object = datetime.datetime.strptime(new_date_string,'%Y-%m-%d %H:%M:%S')

print (type(datetime_object))

one_day=datetime_object + timedelta(days=1)
print(one_day)
print(type(one_day))


#datetime object to text in order to store in csv
object2=datetime_object.strftime("%Y-%m-%d, %H:%M:%S")
print(type(object2))

'''



nlp=spacy.load('el_core_news_lg')

df=pd.read_csv('final.csv',encoding='utf-8',header=0)
#print(df.shape)

#df['Location']=df['Body'].astype(str).apply(lambda x : nlp(x).ents)
#df.to_csv('final2.csv')




df['Location']=df['Body'].apply(lambda x: [entity.text for entity in nlp(x).ents if entity.label_== 'GPE'])


del df['Unnamed: 0']
print(df[:10])
df.to_csv('final3.csv',index=False)



'''
texts = df["Body"].to_list()
ents = []
for doc in nlp.pipe(texts):
    for ent in doc.ents:
        if ent.label_ == "GPE":
            ents.append(ent)
            
print(ents)'''

'''text=pd.Series(df['Body'],dtype='string').to_string()


doc=nlp(text)

for ent in doc.ents:
    if (ent.label_=='GPE'): 
        print(ent.text)
print(len(doc.ents))'''
   
#print(df.shape,df.dtypes)

#print(df.head())

'''
test='2015-02-02'
test2=test[:4]
test3='16 Ιανουαρίου έγινε αυτό'
print(test2)

regex=r"\d+\s+\w+"
match=re.match(regex,test3)
print(match.string)
test4=match.string +' ' + test2
print(test4)



def month_string_to_number(string):
    m = {
        'Ιανο': 1,
        'Φεβρ': 2,
        'Μαρτ': 3,
        'Απριλ':4,
         'Μαι':5,
         'Ιούν':6,
         'Ιούλ':7,
         'Αυγο':8,
         'Σεπτ':9,
         'Οκτ':10,
         'Νοε':11,
         'Δεκ':12
        }
    s = string.strip()[:3].lower()

    try:
        out = m[s]
        return out
    except:
        raise ValueError('Not a month')



        \w{1,2}\s\b[A-Z].*?\b
'''
