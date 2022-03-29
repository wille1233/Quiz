
from random import randint, choice
from re import I
from Classes import *

#Varaibles
points = 0
main_questions = []
questions_counter = 0

with open("questions.txt", "r", encoding="utf8") as f: #Imports questions
    for line in f.readlines():
        attributes = line.split("/")
        char = Questions(attributes[0],attributes[1],attributes[2])
        main_questions.append(char)

if __name__ == "__main__":
    print(f"-= Hello Welcome to this quiz! =- \n")

    for i in main_questions:
        car = i
        car.get_question()
        car.print_alternative()
        human_answer = input("Answer: ").capitalize()
         #Todo Remove the question to prevent reoccurense
        questions_counter += 1 # Counts all the questions
        
        if human_answer in car.check_correct():
            print("The Answer Is Correct!\n")
            points = points + 1
        else:
            print(f"Not correct!\nThe correct answer was {car.check_correct()}\n")

    if points == questions_counter:
        print(f"You got all the points possible! {points} out of {questions_counter}!")
    elif points == 0:
        print(f"You don't know anything about cars! You got {points} points. Try again") 
    else:
        print(f"You got {points} points out of {questions_counter}!")
        


