# ***************************************************************************************
# 
# CODE BY PVM K22 FIRA
# 
# ***************************************************************************************

import pickle
from question_analysis import question_analysis
from create_update_dataset import get_core

def predict(question):
    analysis = question_analysis(question)
    type_of_question = analysis['type']
    core_of_question = get_core(analysis['structure'])
    vectorizer = pickle.load(open("./data/embedding/"+str(type_of_question)+"_vectorizer.pickel", "rb"))
    tfidf = pickle.load(open("./data/embedding/"+str(type_of_question)+"_tfidf.pickel", "rb"))
    core_matrix = tfidf.transform(vectorizer.transform([core_of_question]))
    model = pickle.load(open("./data/model/"+str(type_of_question)+"_model.pickel", "rb"))
    result = model.predict(core_matrix)
    return result[0]

if __name__ == "__main__":
    question = "định nghĩa trái phiếu?"
    respone = predict(question)
    print(respone)