
from random import randint, choice

from pip import main
from Classes import *


points = 0
main_questions = []

with open("questions.txt", "r", encoding="utf8") as f:
    for line in f.readlines():
        attributes = line.split("/")
        char = Questions(attributes[0],attributes[1],attributes[2])
        main_questions.append(char)

if __name__ == "__main__":
    print(f"-= Hello Welcome to quiz! =- \n")

    for i in main_questions:
        car = choice(main_questions)
        car.get_question()
        car.print_alternative()
        human_answer = input("Answer: ").capitalize()
        
        if human_answer in car.check_correct():
            print("Correct!\n")
            points = points + 1
        else:
            print(f"Not correct!\nThe correct answer was {car.check_correct()}\n")

    print(f"You got {points} points!")


