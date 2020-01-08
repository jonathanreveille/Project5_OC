#! /usr/bin/env python3
# coding : utf-8

from models.downloader import ProductDownloader
#from models.manager import ProductManager

import os 

def main():

    name = input("Hello, what's your name buddy?  ")
    name = str(name)
    os.system('clear')

    #Welcome text
    print("Welcome", name,"!")
    print("And welcome to the application Pur-Beurre \n \
           Let me guess, you want to eat more decent food finally, right?")

    # Show the menu of possibilities : MENU 
    print("Which action do you want to do ? \n \
    \n \
    1. You want to find an alternative to a product ? \n \
    2. See list of favorites \n \
    0. To quit the application. \n")

    #while loop
    select = True
    while select:
        #Asking user to select an option
        command = input("Now tell me, what do you want to do ? Please enter a number according to the aboved list: ")
        command = int(command)
        
        #Clear the screen once the user selected his option
        os.system("clear")

        if command == 1:
            print("You have selected : option 1 --> Select a category now to find a product")
            print(" \n \
                   1 - Biscuits \n \
                   2 - Pizza  \n \
                   3 - Pâte à tartiner salé  \n \
                   4 - Confiture  \n \
                   5 - Jus de fruit \n "
                   )
            key = int(input("Please select one number in the aboved list to continue : "))
            
            if key == 1: 
                print("You have selected : Biscuits")
            elif key == 2:
                print("You have selected : Pizza")
            elif key == 3:
                print("You have selected : Pâte à tartiner salé")
            elif key == 4:
                print("You have selected : Confiture")
            elif key == 5:
                print("You have selected : Jus de fruit")


        elif command == 2:
            print("You have selected : option 2 --> You want to see your favorites")
            break

        elif command != 1 or 2:
            print("Quitting the app")
            break   

if __name__ == "__main__":
    main()


# def creating_user(self):
#     """ This method is to say hello to the user and
#     ask for his name """

#     name = input("Please, tell me your name: ")
#     name = str(name)

#     if name in self.names:
#         print("Welcome back", name, "!")

#     elif name not in self.names:
#         self.names.append(name)
#         print("You are a new user, welcome", name)

# while True:
#     command = raw_input('command? ').strip()
#     if command == 'say_hello':
#         print('Hello')
#     elif command == 'other_thing':
#         print('Doing something else')
#     elif command == 'quit':
#         break
#     else:
#         print('Invalid Command.')