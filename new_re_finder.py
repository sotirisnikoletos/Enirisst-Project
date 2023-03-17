import pandas as pd
import re
import regex
import spacy

def monthsf(string):
    months = {
            "Ιανουαρίου": '01',
            "Φεβρουαρίου":'02',
            "Μαρτίου": '03',
            "Απριλίου": '04',
            "Μαΐου ": '05',
            "Ιουνίου": '06',
            "Ιουλίου": '07',
            "Αυγούστου": '08',
            "Σεπτεμβρίου": '09',
            "Οκτωμβρίου": '10',
            "Νοεμβρίου": '11',
            "Δεκεμβρίου": '12',
            "Ιαν.": '01',
            "Φεβρ.": '02',
            "Μαρτ.": '03',
            "Απρ.": '04',
            "Ιουν.": '06',
            "Ιουλ.": '07',
            "Αυγ.": '08',
            "Σεπτ.": '09',
            "Οκτ.": '10',
            "Νοεμ.": '11',
            "Δεκ.": '12'
        }
    

    try:
        out = months[string]
        return out
    except:
        raise ValueError('Not a month')
'''
    parts = str.split().lower()
    day = int(parts[0])
    month = months[parts[1]]
    

    return f"{day:02d}/{month:02d}"

def is_date(text):
    pattern = re.compile("^\d{1,2} (Ιαν|Φεβρ|Μαρτ|Απρλ|Μαΐου|Ιουν|Ιουλ|Αυγούστου|Σεπτεμ|Οκτωμ|Νοεμβρ|Δεκεμβρ)", re.IGNORECASE)
    

    filename = "final3.csv"
        

    df = pd.read_csv(filename)

    for i in range (len(df.index)):
        is_date(df['Body'])
        if(df['Body'].str.contains(pattern).iloc[i]):
            df['Date'].iloc[i]=df['Date'].apply(convert_to_date).iloc[i]


filename = "final3.csv"
        

df = pd.read_csv(filename)
is_date(df['Body'])


file = pd.read_csv('final3.csv')

df = pd.DataFrame(file)




df['New']=df['Body'].str.extract(r"\d{1,2}\s(Ιαν|Φεβρ|Μαρτ|Απρλ|Μαΐου|Ιουν|Ιουλ|Αυγούστου|Σεπτεμ|Οκτωμ|Νοεμβρ|Δεκεμβρ)")

for i in range (len(df.index)):
    
    df['New']=df['New'].map(months).astype(int)
    
print(df.head())
df.to_csv('test4.csv')

    
text='10 Ιουλίου'

pattern=re.match(r"\d{1,2}\s(Ιαν|Φεβρ|Μαρτ|Απρλ|Μαΐου|Ιουν|Ιουλ|Αυγούστου|Σεπτεμ|Οκτωμ|Νοεμβρ|Δεκεμβρ)",text).group(1)
print(monthsf(pattern))

new_text=text + str(monthsf(pattern))

print(new_text)

new_text2 = re.findall(r'\d',new_text)
new_text=new_text2
print(new_text2)



\w{1,2}\s\b[A-Z].*?\b[.]{0,1}
\w{1,2}\s\W+$

text='Στις 25 Αυγ. έγινε αυτό '
match1=regex.compile(r'\d{1,2}\s\p{Greek}{3,20}[.]{0,1}')
res=match1.findall(text)

res2=''.join(res)
res3=res2.split()
print(res3[1])

file=pd.read_csv('final3.csv',encoding='utf-8')
df=pd.DataFrame(file)



for i in range (len(df.index)):
    #df['Date2'].iloc[i]=df['Date2'].str.split().iloc[i]
    match1=regex.compile(r'\d{1,2}\s\p{Greek}{3,20}[.]{0,1}')
    try:
        res=match1.findall(df['Body'].iloc[i])
        res2=''.join(res)
        res3=res2.split()
        if (monthsf(res3[1])):
            print(df['Titles'].iloc[i])

            year=df['Date2'].str[:4].iloc[i]
        
            day=res3[0]

            df['Date2'].iloc[i]=year+'-'+ monthsf(res3[1])+'-'+day+' '+df['Date2'].str[11:].iloc[i]
            df.to_csv('finalllll.csv')  

    except:
        pass
    
    df.to_csv('finalllll.csv')  
    

#print(monthsf(res3[1]))'''



nlp=spacy.load('el_core_news_lg')

df=pd.read_csv('finalllll.csv',encoding='utf-8',header=0)

def tokenize_text(text):
    doc = nlp(text)
    return [token.text for token in doc if not token.is_punct and not token.is_space]

df['Body'] = df['Body'].apply(tokenize_text)
print(df.head())

def remove_stopwords(text_list):
    cleaned_list = []
    for text in text_list:
        doc = nlp(text)
        tokens = [token.text for token in doc if not token.is_stop]
        cleaned_text = ' '.join(tokens)
        cleaned_list.append(cleaned_text)
    return cleaned_list

# Example usage

df['Body'] = df['Body'].apply(remove_stopwords)
print(df.head())
df.to_csv('thebest_tokenized_stopwords.csv')