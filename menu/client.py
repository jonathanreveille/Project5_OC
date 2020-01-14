#! /usr/bin/env python3
# coding : utf-8

from .menu import Menu

class Client:


    def __init__(self):
        self.running = False # acts like a switch  ON/OFF
        self.next  = self.menu0
        self.params = {}


    def start(self):
        """ this method is the loop  to  make the application launch """
        
        self.running = True # the switch is turned ON

        while self.running:

            self.next() #points toward the method menu0, defined in attributes


    def menu0(self):
        """ This menu will ask the user what he wishes to 
        do on the application """

        print("Dans self.params: ", self.params)
        
        menu = Menu(["Recherches-tu un produit ? ", "Voir sa liste de produit favoris"])

        while True:
            print(menu)
            choice = input(">>>  ")

            if menu.is_valid_choice(choice):
                self.next = self.menu1
                self.params["action"] = menu[choice]
                break


    def menu1(self):

        print("Dans self.params", self.params)

        menu = Menu(["Biscuits", "Pizza", "Pâte à tartiner", "Confitures", "Pâte à tartiner salée", "HOME", "QUIT"])

        while True:
            print(menu)
            choice =  input(">>>  ")

            if menu.is_valid_choice(choice):
                self.next = self.menu2
                entry = menu[choice]
                self.params["category"] = entry
                
                if entry == "QUIT":
                    self.next = self.quit_app

                elif entry == "HOME":
                    self.next = self.menu0
                    self.params = {}

            break


    def menu2(self):
        """ this method is to show the menu of products
        for the client's interface """

        print("Dans self.params", self.params)
        
        menu = Menu(["product 1", "product 2", "product 3", "product 4", "HOME", "QUIT"])

        while True:

            print(menu)
            choice =  input(">>>  ")

            if menu.is_valid_choice(choice):
                self.next = self.menu3
                entry = menu[choice]
                self.params["product"] = entry

                if entry == "QUIT":
                    self.next = self.quit_app

                elif entry == "HOME":
                    self.next = self.menu0
                    self.params = {}

            break


    def menu3(self):
        """ THis method is to show the menu of substitutes products
        for the client's interface """

        print("Dans self.params", self.params)

        menu = Menu(["substitute 1", "substitute 2", "substitute 3", "substitute 4", "HOME", "QUIT"])

        while True:

            print(menu)
            choice =  input(">>>  ")

            if menu.is_valid_choice(choice):
                self.next = self.quit_app

                entry = menu[choice]
                self.params["substitute"] = entry
                if entry == "QUIT":
                    self.next = self.quit_app

                elif entry == "HOME":
                    self.next = self.menu0
                    self.params = {}

            break


    def quit_app(self): 
        """ This method manages the option quit 
        from the menu for the client's interface """

        print("Dans self.params", self.params)

        quit_yes_or_no = input(">>> Do you really want to quit ? Y / N :  ")
        
        if quit_yes_or_no == "Y":
            self.running = False
            print("Good Bye")

        elif quit_yes_or_no  ==  "N":
            self.running = True 
            self.next = self.menu0



client = Client()
client.start()