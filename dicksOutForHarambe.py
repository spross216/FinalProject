import csv
import random

filename = 'test.csv'
currentQuestion = 2 

with open(filename, mode='r') as file:
    reader = csv.DictReader(file)
    questions = [row for row in reader]

def loadQuestion():
    setQuestion = questions[currentQuestion]
    prompt = setQuestion['question']
    print(prompt)
    options = []
    answer = setQuestion['answer']
    options.append(setQuestion['answer'])
    options.append(setQuestion['decoy1'])
    options.append(setQuestion['decoy2'])
    options.append(setQuestion['decoy3'])
    random.shuffle(options)
    print(options)
    if answer == options[0]:
        print('correct')
    else:
        print('incorrect')

loadQuestion()





