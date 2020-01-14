#! /usr/bin/env python3
# coding : utf-8

import os
import time
from exception.unvalid import UnvalidInput


class Menu:

    def __init__(self, name):
        self.name = name
        self.favorited_list = {} #key will be the product to replace, AND , the value will be the product that replaces it


    def show_main_menu(self):
        """ This method is to show the menu and select a choice """

        os.system('clear') #clear terminal screen

        print("Welcome", self.name,", what do you wish to do today ? \n \
            \n \
            1. You want to find an alternative to a product ? \n \
            2. See your list of favorite products \n \
            0. Quit the app \n "
            )

        try:
            selection = int(input("Please select one choice (number only): "))

        except ValueError as e:
            print(e, "Please, use a VALID number from list")
            time.sleep(3)
            self.show_main_menu()

        return self.select_in_menu(selection)


    def select_in_menu(self, selection):
        """ This method is to select an option in the menu"""
        
        os.system('clear')

        if selection == 1: 
            print("The option you have chosen is the 1st,\
            do you want to seek for a new product?")
            self.show_category()

        elif selection == 2:
            print("Do you want to see your list of favorites?")
            self.look_at_favorites()

        elif selection == 0:
            print("It was nice to you see again, see ya soon buddy!")
            quit()

        else:
            print("WARNING : Please insert a number from list above only")
            time.sleep(3)
            self.show_main_menu()


    def show_category(self):
        """ This method is to choose a category after the 1st 
        step of the menu phase"""

        os.system('clear')

        print("\
>>>> Here are all the categories, choose one : \n \
                   1 - Biscuit \n \
                   2 - Pizza  \n \
                   3 - Salted pastes (Pâte à tartiner salé)  \n \
                   4 - Jam (Confiture)  \n \
                   5 - Juices (Jus de fruit) \n \
                   0 - <<< Back To Menu >>> "
                   )
        try:
            key = int(input("Please, enter your choice (number only): "))

        except ValueError as e: #if another type of data but integers
            print(e, "No strings please, use only VALID number from list")
            time.sleep(3)
            self.show_category()

        return self.selecting_a_category(key)


    def go_back_to_main_or_quit(self):
        """ This method allows you to come back to the main menu
        or quit the application"""

        a = input("Press ""B"" to return to menu or ""Q"" to quit: ").upper()

        if a == "B":
            return self.show_main_menu()

        elif a == "Q":
            print("see you next time buddy, eat better !")
            quit()


    def selecting_a_category(self, key):
        """ This method is to select a category from the 
        category menu """

        if key == 1:
            print("you have selected the category : Biscuits")
            self.go_back_to_main_or_quit()

        elif key == 2:
            print("You have selected the category : Pizza")
            self.go_back_to_main_or_quit()

        elif key == 3:
            print("You have selected the category : Pâte à tartiner salée")
            self.go_back_to_main_or_quit()

        elif key == 4:
            print("You have selected the category : Confiture")
            self.go_back_to_main_or_quit()

        elif key == 5:
            print("You have selected the category : Jus de fruit")
            self.go_back_to_main_or_quit()

        elif key == 0:
            self.show_main_menu()

        elif key != int():
            print("Please insert a valid number from the list, try again")
            time.sleep(3)
            self.show_category()


    def look_at_favorites(self):
        """ This method is to get all our favorites """

        print("Last updated favorite list : ", self.favorited_list)
        self.go_back_to_main_or_quit()

    def do_something(self):
        pass


if __name__ == "__main__":

    name = str(input("Welcome to Pur-Beurre, what's your name buddy ?  "))
    a = Menu(name)
    a.show_main_menu()


