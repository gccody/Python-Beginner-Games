from random import *
import os

def numberToGuess(min, max):
    number = randint(min,max)
    return number

def higherLower(number, guess):
    if(guess > number):
        return 1
    elif(guess < number):
        return -1
    else:
        return 0

def getGuess(min, max):
    while True:
        while True:
            try:
                guess = int(input("Guess a number between " + str(min) + " and " + str(max) + ": "))
                break
            except ValueError:
                print("Please enter a number")
                input("Press enter to continue... ")
        if (guess >= min and guess <= max):
            break
        else:
            print("You entered an invlaid number out of range.")
            input("Press enter to continue... ")
    return guess
    

def getMin():
    while True:
        try:
            min = int(input("Enter the minimum number you want to guess: "))
            break
        except ValueError:
            print("Please enter a valid number")
            input("Press eneter to continue... ")
            os.system('cls')
    return min

def getMax():
    os.system('cls')
    while True:
        try:
            max = int(input("Enter the maximum number you want to guess: "))
            break
        except ValueError:
            print("Please enter a valid number")
            input("Press enter to continue... ")
            os.system('cls')
    os.system('cls')
    return max

def main():
    os.system('cls')

    while True:
        os.system('cls')
        min = getMin()
        max = getMax()
        number = numberToGuess(min, max)
        while True:
            guess = getGuess(min, max)
            if (higherLower(number, guess) == 1):
                print("The number is lower!")
            elif(higherLower(number, guess) == -1):
                print("The number is higher!")
            else:
                print("You guessed it!")
                break
        while True:
            cont = input("\nWould you like to play agian? (y/n)")
            cont.lower()
            if (cont == "y" or cont == "n"):
                break
            else:
                os.system('cls')
                print("You entered an invalid answer please try again")
                input("Press enter to continue... ")
                os.system('cls')
        if (cont == "n"):
            break

    os.system('cls')
    input("Press enter to go back to main menu... ")
    os.system("Main.py")

if __name__ == '__main__':
    main()