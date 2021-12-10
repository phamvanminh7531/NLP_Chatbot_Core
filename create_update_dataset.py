# ***************************************************************************************
# 
# CODE BY PVM K22 FIRA
# 
# ***************************************************************************************

from question_analysis import question_analysis
import csv

f_full = open('./data/corpus/full_corpus.txt', 'r', encoding='utf-8-sig')

question_list = []
answer_list = []

for x in f_full:
    if "?" in x:
        question_list.append(x.strip())
    else:
        answer_list.append(x.strip())

class QA():
    def __init__(self, type, core_token, respone):
        self.type = type
        self.core_token = core_token
        self.respone = respone
    
    def __str__(self) -> str:
        return self.core_token

def get_core(structure):
    core = []
    for i in structure:
        if i[1] == '<core>':
            core.append(i[0])
    result = ' '.join(core)
    return result


if __name__ == "__main__":
    listQA = []

    for i in question_list:
        index = question_list.index(i)
        respone = answer_list[index]
        q_analysis = question_analysis(i)
        question_type = q_analysis['type']
        core_token = get_core(q_analysis['structure'])
        __aQA = QA(type=question_type, core_token=core_token, respone=respone)
        listQA.append(__aQA)


    with open('./data/dataset.csv', mode='w', encoding='utf-8-sig') as csv_file:
        fieldnames = ['type', 'core', 'respone']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for i in listQA:
            writer.writerow({'type': str(i.type), 'core':i.core_token, 'respone':i.respone})