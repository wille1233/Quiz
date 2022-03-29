#Quiz questions
from random import randint





class Questions:
    
    def __init__(self, question : str, answer : str, alternatives : str):
        self.question = question
        self.answer = answer
        self.alternatives = alternatives


    def __str__(self):
        return self.question

    def get_question(self):
        print(self.question)
        return self.question


    def check_correct(self):
        return self.answer

    def print_alternative(self):
        print(self.alternatives)
        return self.alternatives

#class Quiz:
    #def __init__(self, name, questions):
        self.name = name
        self.questions = questions

    #def get_question(self):
        return questions_list[randint(0, questions_list_length)]
