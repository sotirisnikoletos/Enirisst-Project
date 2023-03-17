

'''


import gensim

import pandas as pd
import numpy as np
import fasttext

# Load the pre-trained FastText model using KeyedVectors
model = gensim.models.keyedvectors.load_word2vec_format('cc.el.300.vec')

# Load the text data from the CSV file
df = pd.read_csv('thebest_tokenized_stopwords.csv',header=0,encoding='latin')
texts=df['Body'].tolist()
embeddings = []
for text in texts:
     words = text.split() 
     avg_vector = np.zeros((model.vector_size)) 
     for word in words: 
        if word in model.key_to_index: 
            avg_vector += model[word] 
            avg_vector /= len(words)
            embeddings.append(avg_vector)
#print(embeddings)
#embeddings = np.array(embeddings)
#np.save('embeddings_thebest.npy',embeddings)

result = model.most_similar(positive=['γυναίκα', 'βασιλιάς'], negative=['άντρας'])
most_similar_key, similarity = result[0]  # look at the first match
print(f"{most_similar_key}: {similarity:.4f}")
    

import spacy
import pandas as pd
import numpy as np

# load the spacy model
nlp = spacy.load("el_core_news_lg")

# load the csv file
df = pd.read_csv("thebest_lat_long_keywords.csv")

# create a list to store the word vectors
word_vectors = []

# iterate through each row in the dataframe
for index, row in df.iterrows():
    # get the text from the 'body' column
    text = row['Body']
    # create a Spacy document
    doc = nlp(text)
    # get the mean vector for the document
    mean_vector = doc.vector
    # append the mean vector to the list
    word_vectors.append(mean_vector)

# create a new dataframe to store the word vectors
df_vectors = pd.DataFrame(word_vectors)

# save the dataframe to a CSV file
df_vectors.to_csv("your_vectors_file.csv", index=False)

df2=pd.read_csv('your_vectors_file.csv')
print(df2.shape)

word_vectors_array = np.array(word_vectors)

# save the numpy array to a file
np.save('your_vectors_file.npy', word_vectors_array)'''


'''


# create a list to store the word vectors
word_vectors = []

# iterate through each row in the dataframe
for index, row in df.iterrows():
    # get the text from the 'body' column
    text = row['Body']
    # split the text into words
    words = text.split()
    # create a list to store the word vectors for this document
    document_vectors = []
    # iterate through each word in the document
    for word in words:
        # check if the word is in the vocabulary of the model
        if word in w2v_model.key_to_index:
            # if the word is in the vocabulary, get its vector and append it to the list
            vector = w2v_model[word]
            document_vectors.append(vector)
    # if the document has at least one word in the vocabulary, concatenate the word vectors for the document
   

# convert the list of word vectors to a numpy array
word_vectors_array = np.array(document_vectors)
np.save('your_vectors_file2.npy', word_vectors_array)
# print the shape of the resulting array
print(word_vectors_array.shape)
'''
import gensim

import pandas as pd
import numpy as np
import nltk

from gensim.models import KeyedVectors
w2v_model = gensim.models.KeyedVectors.load_word2vec_format('cc.el.300.vec')
#print(model.most_similar("γιορτή"))
#text=['αύριο','Νίκος','Αθήνα','πυρκαγιών','έκρηξη']
def get_word_embeddings(words):
    embeddings = []
    for word in words:
        if word in w2v_model:
            embeddings.append(w2v_model[word])
    return embeddings

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('body_column_thebest.csv')

# Get the word embeddings for each word in the desired column
embeddings = df['Body'].apply(get_word_embeddings)
# Print the resulting embeddings
print(embeddings)
embeddings = np.array(embeddings)
np.save('greek_embs_thebest.npy',embeddings)



#kanei 5 lepta, dokimazoume me favebook load vectors kai zip fasttext model