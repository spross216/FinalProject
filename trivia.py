'''Since this assignment was meant to be a GUI application, I wanted to take the opportunity to 
write this as a simple implementation of a Model View Controller (MVC) architecture to separate the clas objects responsibilities
and get some practice on tried and true software design methods'''

# The Model

import csv
import random

class DataHandler:

    def __init__(self, filename):

        self.filename = filename
        self.currentQuestion = 0
        self.pullQuestion = []
        self.questions = []
        self.options = []
        self.questionPrompt = ''
        self.answer = ''
        self.score = 0
        
    
    def parseCsv(self):

        with open(self.filename, mode='r') as file:
            reader = csv.DictReader(file)
            self.questions = [row for row in reader]
        self.totalQuestions = len(self.questions)

    def shuffleQuestions(self):

        random.shuffle(self.questions)
    
    def pullQuestionAndAnswers(self):

        self.pullQuestion = self.questions[self.currentQuestion]
    
    def loadPrompt(self):

        self.questionPrompt = self.pullQuestion['question']
    
    def loadAnswer(self):

        self.answer = self.pullQuestion['answer']
    
    def loadAnswerOptions(self):

        self.options.append(self.pullQuestion['answer'])
        self.options.append(self.pullQuestion['decoy1'])
        self.options.append(self.pullQuestion['decoy2'])
        self.options.append(self.pullQuestion['decoy3'])

    def shuffleAnswerOptions(self):

        random.shuffle(self.options)
    
    def checkAnswer(self, answer: str):

        if self.answer == answer:
            self.score += 1
            return True
        else:
            return False
    
    def nextQuestion(self):
        
        if self.totalQuestions > self.currentQuestion:
            self.currentQuestion += 1
            return True
        else:
            return False
    
    def totalScore(self):
        
        self.finalScore = (self.score / self.totalQuestions) * 100
        self.finalScoreMessage = (
            f'You answered {self.score} out of {self.totalQuestions}\
             correctly for a total score of {self.finalScore}%'
        )

# the View

import tkinter as tk
from tkinter import messagebox

class Gui:

    def __init__(self, master, controller):

        self.master = master
        self.controller = controller
        self.selectedOption = tk.StringVar()

    def createTestFrame(self):

        self.testFrame = tk.Frame(
            self.master, 
            bd=2, 
            highlightthickness=2, 
            highlightcolor='dark blue', 
            bg='white'
        )

        self.testFrame.pack()
    
    def createButtonFrame(self):

        self.buttonFrame = tk.Frame(
            self.master, 
            bd=2,
            highlightthickness=2,
            highlightcolor='dark blue',
            background='white'
        )

        self.buttonFrame.pack()
    
    def createTestPrompt(self):

        self.testPrompt = tk.Label(
            self.testFrame, 
            text='', 
            bg='white', 
            fg='dark blue'
        )

        self.testPrompt.pack(side=tk.TOP, padx=10, pady=10)
    
    def createRadioButtons(self):

        self.radioButtons = []

        self.buttonOptions = [
            'Option 1', 
            'Option 2', 
            'Option 3', 
            'Option 4'
        ]

        for self.option in self.buttonOptions:

            self.radioButton = tk.Radiobutton(
                self.testFrame, 
                bg='white', 
                text=self.option, 
                variable=self.selectedOption,
                value=self.option
            )

            self.radioButton.pack(
                side=tk.BOTTOM, 
                anchor=tk.W, 
                padx=10, 
                pady=10
            )

            self.radioButtons.append(self.radioButton)
            

    def configureRadioButtons(self, text: list):

        for i, self.radioButton in enumerate(self.radioButtons):
            self.radioButton.configure(text=text[i])

    def createButtons(self):

        self.submitButton = tk.Button(
            self.buttonFrame, 
            text='Submit',
            command=self.controller.submitButtonPress
        )

        self.submitButton.pack(
            side=tk.LEFT,
            padx=10,
            pady=10
        )

        self.nextButton = tk.Button(
            self.buttonFrame,
            text='Next',
            command=self.controller.nextButtonPress
        )

        self.nextButton.pack(
            side=tk.LEFT,
            padx=10,
            pady=10
        )

    def popUpMessageCorrect(self):

        messagebox.showinfo('Trivia My.CSV', "Correct! :-)")
    
    def popUpMessageIncorrect(self):

        messagebox.showinfo('Trivia My.CSV', 'Incorrect :-(')
    
    def disableButtons(self):

        self.submitButton.configure(state='disabled')
        self.nextButton.configure(state='disabled')
        for self.radioButton in self.radioButtons:
            self.radioButton.configure(state='disabled')


# the controller

import sys

class Trivia:

    def __init__(self, filename):

        self.filename = filename
        self.model = DataHandler(self.filename)
        self.master = tk.Tk()
        self.view = Gui(self.master, self)

    def initView(self):

        self.master.title('Trivia My.CSV')
        self.master.geometry('800x400')
        self.master.configure(bg='white')
        self.view.createTestFrame()
        self.view.createButtonFrame()
        self.view.createTestPrompt()
        self.view.createRadioButtons()
        self.view.createButtons()
        self.view.master.mainloop()
    
    def initModel(self):

        self.model.parseCsv()
        self.model.shuffleQuestions()

    def loadQuestion(self):
        
        self.model.pullQuestionAndAnswers()
        self.model.loadPrompt()
        self.model.loadAnswer()
        self.model.loadAnswerOptions()
        self.model.shuffleAnswerOptions()
        self.view.testPrompt.configure(text=self.model.questionPrompt)
        self.view.configureRadioButtons(self.model.options)

    def submitButtonPress(self):

        self.model.checkAnswer(self.view.selectedOption)
        if self.model.checkAnswer == True:
            self.view.popUpMessageCorrect()
        else: 
            self.view.popUpMessageIncorrect()
    
    def nextButtonPress(self):

        self.model.nextQuestion()
        if self.model.nextQuestion == True:
            self.loadQuestion()
            self.startGame()
        else:
            self.view.disableButtons()
            self.model.totalScore()
            self.view.testPrompt.configure(text=self.model.finalScoreMessage)
            

if __name__ == '__main__':
    filename = sys.argv[1]
    game = Trivia(filename)
    game.initModel()
    game.initView()
    game.loadQuestion()
    


    

    



