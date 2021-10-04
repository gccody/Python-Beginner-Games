import os
import time
def main():
    os.system('cls')
    print("Enter the number of the game you would like to play:")
    print("=======================================================")
    print("1) Guess the number")
    print("2) Hangmaen")
    print("3) Random password generator")
    print("4) Rock Paper Scissors")
    print("5) Sorting Method")
    print("0 to close")

    while True:
        while True:
            try:
                game = int(input("\nWhich game would you like to play?: "))
                break
            except ValueError:
                print("Please enter a number... ")
        if (game >= 0 and game <= 5):
            break

    if (game == 1):
        time.sleep(1)
        os.system("Guess-The-Number.py")
    elif (game == 2):
        time.sleep(1)
        os.system("Hangman.py")
    elif (game == 3):
        time.sleep(1)
        os.system("RandomPasswordGenerator.py")
    elif (game == 4):
        time.sleep(1)
        os.system("Rock-Paper-Scissors.py")
    elif (game == 5):
        time.sleep(1)
        os.system("Sorting-Method.py")
    elif (game == 0):
        print("\nGoodbye")
        input("Press enter to close..")


            

if __name__ == '__main__':
    main()