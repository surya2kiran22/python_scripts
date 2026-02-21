import random

def number_guesser(turn: int):
    num = random.randrange(1)
    i=0
    while True:
        num1 = int(input("enter a number under 100: "))
        if num1 == num :
            print("you won")
            return "You won"
            break
        elif num1 > num: #50 > 30
            print("num is more so add less than ", num1)
        elif num1 < num: #20 < 30
            print("num is less so add more than ", num1)
        i = i+1
        if i == turn:
            print("you lost")
            print("the number is ", num)
            return "You lost"
            break



turns = int(input("enter number of turns: "))
number_guesser(turns)






