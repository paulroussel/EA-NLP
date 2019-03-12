import os.path
from gensim import corpora
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
import pandas as pd
import nltk
from nltk.stem.porter import PorterStemmer
porter_stemmer = PorterStemmer()
from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()
import nltk.internals
from gensim import corpora, models
from numpy import dot
from numpy.linalg import norm
from collections import defaultdict
import nltk
import string
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
import nltk
import string
import re

from nltk.stem.snowball import FrenchStemmer



def remove_punct(text):
    text  = "".join([char for char in text if char not in string.punctuation])
    text = re.sub('[0-9]+', '', text)
    return text

def tokenization(text):
    text = re.split('\W+', text)
    return text

stopword = nltk.corpus.stopwords.words('french')

def remove_stopwords(text):
    text = [word for word in text if word not in stopword]
    return text

stemmer = FrenchStemmer()

def stemming(text):
    text = [stemmer.stem(word) for word in text]
    return text

wn = nltk.WordNetLemmatizer()

def lemmatizer(text):
    text = [wn.lemmatize(word) for word in text]
    return text


def vec2string (list):
    return(' '.join(list))


def preprocessing(df,nom_colonne):
    df[nom_colonne] = df[nom_colonne].apply(lambda x: remove_punct(x))
    df[nom_colonne] = df[nom_colonne].apply(lambda x: tokenization(x.lower()))
    df[nom_colonne] = df[nom_colonne].apply(lambda x: remove_stopwords(x))
    df[nom_colonne] = df[nom_colonne].apply(lambda x: stemming(x))
    df[nom_colonne] = df[nom_colonne].apply(lambda x: lemmatizer(x))
    df[nom_colonne] = df[nom_colonne].apply(lambda x: vec2string(x))
    return(df)
