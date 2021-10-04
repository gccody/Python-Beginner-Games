import os

def instructions():
    print("This is a two player game. \nThe first player will choose the word. \nThe second player will try and guess it. \nYou get 6 misses to guess the word")
    input("Press enter to continue... ")

def check(word, guess):
    a = []
    for i in range(len(word)):
        if (word[i] == guess.lower()):
            a.append(i)
    if(a == []):
        return 0
    else:
        return a


def playerOne():
    word = input("\nEnter word you would like to be guessed: ")
    return list(word.lower())

def hideWord(word):
    a = []
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for char in word:
        if (char not in letters):
            a.append(char)
        else:
            a.append("_")
    return a

def listToString(hidden):
    a = ""
    for char in hidden:
        a += char
    return a

def playerTwo(word, hidden):
    os.system('cls')

    final = word

    misses = 6

    while True:
        print(listToString(hidden))
        while True:
            guess = input("Enter one letter: ")
            if (len(guess) == 1):
                break
            else:
                print("Please enter one letter")
        if (check(word, guess) == 0):
            print("That letter is not apart of the word. \nPlease try again. ")
            misses -= 1
        else:
            a = check(word, guess)
            for char in a:
                hidden[char] = guess.lower()

        if(misses < 0):
            break

        if(hidden.count("_") == 0):
            break
        else:
            print("You have " + str(misses) + " misses left!")
    
    if (hidden.count("_") == 0):
        print(listToString(word))
        print("You guessed it!")
    else:
        print("You failed. \nThe word is... " + listToString(word))

def main():
    while True:
        os.system('cls')
        instructions()
        word = playerOne()
        hidden = hideWord(word)
        playerTwo(word, hidden)
        while True:
            cont = input("Would you like to play again? (y/n):  ")
            cont.lower()
            if(cont == "yes" or cont == "y" or cont == "no" or cont == "n"):
                break
            else:
                print("Please enter (y/n)")
                input("Press enter to continue... ")
        if(cont == "no" or cont == "n"):
            break
    os.system('cls')
    input("Please press enter to return to menu... ")
    os.system("Main.py")

if __name__ == '__main__':
    main()