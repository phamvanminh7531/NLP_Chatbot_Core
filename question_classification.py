import json
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import svm
from re_processing import question_re_processing_without_token

with open('./data/question.json', 'r', encoding='utf-8-sig') as f:
    questions = json.load(f)

train_x = []

train_y = []

for i in questions['questions']:
    for x in i['patterns']:
        train_x.append(x)
        train_y.append(i['type'])


vectorizer = CountVectorizer(binary=True)
train_x_vectors = vectorizer.fit_transform(train_x)

cls_svm = svm.SVC(kernel='linear')
cls_svm.fit(train_x_vectors, train_y)

def question_classification(question):
    clean_question = question_re_processing_without_token(question)
    vector = vectorizer.transform([clean_question])
    result = cls_svm.predict(vector)
    return result[0]

if __name__ == "__main__":
    test = "Cần bao nhiều tiền để có thể đầu tư cổ phiếu?"
    print(question_classification(test))