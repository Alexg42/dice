# This is a simulated Dice rolling program

import random

min = 1
roll = True

print("This is a simulated Dice rolling program. Please type how many sides the dice should have: ")

max = int(input())

def rollDice(max):
    print (random.randint(min, int(max)))
    
while (roll == True):
    rollDice(max)
    


    
