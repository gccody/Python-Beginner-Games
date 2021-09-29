from random import randint
import time
import os

wStreak = 0
lStreak = 0
tStreak = 0
wBest = 0
lBest = 0
tBest = 0

def aiAnswer():
    a = randint(0,2)
    alist = ["rock", "paper", "scissors"]
    a = alist[a]
    return a

def getGuess():
    print("Enter your guess")
    guess = input("Rock paper scissors ... ")
    guess.lower()
    return guess

def winCheck(a, guess):
    if ((a == "rock" and guess == "paper") or (a == "paper" and guess == "scissors") or (a == "scissors" and guess == "rock")):
        return 1
    elif (a == guess):
        return 2
    else:
        return 0

while True:
    a = aiAnswer()
    guess = getGuess()
    print("I guess ... " + a)
    b = winCheck(a, guess)

    if(b == 1):
        print("\nYou Win!")
        wStreak += 1
        lStreak = 0
        tStreak = 0
        print("You are on a win streak of " + str(wStreak))
        if(wStreak > wBest):
            wBest = wStreak
    elif(b == 2):
        print("\nWe Tied")
        wStreak = 0
        lStreak = 0
        tStreak += 1
        print("You are on a tie streak of " + str(tStreak))
        if(tStreak > tBest):
            tBest = tStreak
    else:
        print("\nYou Lost")
        wStreak = 0
        lStreak += 1
        tStreak = 0
        print("You are on a losing streak of " + str(lStreak))
        if(lStreak > lBest):
            lBest = lStreak
    
    print("\nMost wins in a row : " + str(wBest))
    print("Most loses in a row: " + str(lBest))
    print("Most ties in a row: " + str(tBest))
    
    c = input("\nWould you like to continue? (y/n) ")
    c.lower()
    if (c == "n"):
        break

    os.system('cls')
os.system('cls')
print("Most wins in a row : " + str(wBest))
print("Most loses in a row: " + str(lBest))
print("Most ties in a row: " + str(tBest))
print("\nGoodBye")

time.sleep(3)