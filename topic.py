import pandas as pd
import numpy as np
import gensim
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
from nltk.stem import WordNetLemmatizer, SnowballStemmer
from nltk.stem.porter import *
import nltk
nltk.download('wordnet')

# Preprocessing function
def preprocess(text):
    result = []
    for token in gensim.utils.simple_preprocess(text):
        if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 3:
            result.append(WordNetLemmatizer().lemmatize(token, pos='v'))
    return result

# Load the csv file
df = pd.read_csv("thebest_tokenized_stopwords.csv")

# Preprocess the text data
processed_docs = df['Body'].map(preprocess)

# Create a dictionary from the preprocessed data
dictionary = gensim.corpora.Dictionary(processed_docs)

# Filter out tokens that appear in less than 5 documents or more than 0.5 of the documents
dictionary.filter_extremes(no_below=5, no_above=0.5)

# Create a corpus from the dictionary
corpus = [dictionary.doc2bow(doc) for doc in processed_docs]

# Train the LDA model
lda_model = gensim.models.LdaModel(corpus=corpus, id2word=dictionary, num_topics=100, random_state=100, update_every=1, chunksize=100, passes=10, alpha='auto', per_word_topics=True)

# Print the topics
for idx, topic in lda_model.print_topics():
    print("Topic: {} \nWords :{}".format(idx,topic))
    