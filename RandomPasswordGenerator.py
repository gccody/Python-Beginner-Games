from random import *
import os

os.system('cls')

def getPassword():
    length = randint(20, 30)

    llist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '&',]
    shuffle(llist)

    password = ""

    for i in range(length):
        symbol = llist[randint(0, len(llist) - 1)]
        password += symbol
    return password

def main():
    os.system('cls')
    password = getPassword()
    print(password)
    input("Press enter to return to menu..")
    os.system("Main.py")

if __name__ == '__main__':
    main()