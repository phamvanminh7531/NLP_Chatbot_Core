# ***************************************************************************************
# 
# CODE BY PVM K22 FIRA
# 
# ***************************************************************************************

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import pickle
from sklearn.naive_bayes import MultinomialNB

dataset = pd.read_csv('./data/dataset.csv', encoding='utf-8-sig')

type_list = dataset['type']
core_list = dataset['core']
respone_list = dataset['respone']

type_unique_list = list(set(type_list))

all_QA = list(zip(type_list, core_list, respone_list))

for type in type_unique_list:
    x_train = [core[1] for core in all_QA if core[0]==type]
    y_train = [core[2] for core in all_QA if core[0]==type]
    count_vectorizer = CountVectorizer()
    count_vectorizer.fit_transform(x_train)
    freq_term_matrix = count_vectorizer.transform(x_train)
    tfidf = TfidfTransformer(norm = "l2")
    tfidf.fit(freq_term_matrix)
    tf_idf_matrix = tfidf.fit_transform(freq_term_matrix)
    pickle.dump(count_vectorizer, open("./data/embedding/"+str(type)+"_vectorizer"+".pickel", "wb"))
    pickle.dump(tfidf, open("./data/embedding/"+str(type)+"_tfidf"+".pickel", "wb"))
    model = MultinomialNB(alpha=0)
    model.fit(tf_idf_matrix, y_train)
    pickle.dump(model, open("./data/model/"+str(type)+"_model"+".pickel", "wb"))