from random import *
import os

def main():
    os.system('cls')

    llist = []

    for i in range(100):
        llist.append(randint(0,100))

    print(llist)
    llist.sort()
    print(llist)

    input("Press enter to return to menu...")
    os.system("Main.py")

if __name__ == '__main__':
    main()