import random

def number_guesser(num: int):
    num = num
    i=0
    while True:
        num1 = int(input("enter a number under 100: "))
        if num1 == num :
            print("you won")
            #return "You won"
            return i
            break
        elif num1 > num: #50 > 30
            print("add less than ", num1)
        elif num1 < num: #20 < 30
            print("add more than ", num1)
        i = i+1
        


players = int(input("enter number of players: "))
a = []
num = random.randrange(100)
for i in range(players):
    a.append(number_guesser(num))

min_turn = min(a)
won = a.index(min_turn) +1
print("player won is ", won)





