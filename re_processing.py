from os import environ
from underthesea import word_tokenize

stop_word_file = open('./data/corpus/stopword.txt', 'r', encoding='utf-8-sig')
stop_word_list = [i.strip().lower() for i in stop_word_file]

special_character = [',','!','?','<','>','@','#','$','%','^','&','*','(',')','-','+','[',']','{','}',':','-',':',';','/','+','-','=', '.', '"', '‘', '’']

def question_re_processing_without_token(question):
    result = ""
    for character in question.lower():
        if character not in special_character:
            result+=character
    return result

def question_re_processing_to_token(question):
    result = []
    for token in word_tokenize(question.lower()):
        if token in special_character or token in stop_word_list:
            continue
        else:
            result.append(token)
    return result

if __name__ == "__main__":
    test = "Tôi và bạn có nên chơi chứng khoán không?"
    print(question_re_processing_to_token(test))
    print(stop_word_list)
