#! /usr/bin/env python3
# coding : utf-8

from .menu import Menu

class Client:

    def __init__(self):
        self.running = False # acts like a switch  ON/OFF
        self.next  = self.menu1
        self.params = {}

    def start(self):
        """ this method is the loop  to  make the application launch """
        
        self.running = True

        while self.running:
            self.next()


    def menu1(self):

        print("Dans self.params", self.params)
        menu = Menu(["Biscuits", "Pizza", "Pâte à tartiner", "Confitures", "Pâte à tartiner salée", "quit"])
        
        while  True:
            print(menu)
            choice =  input(">>>  ")

            if menu.is_valid_choice(choice):
                self.next = self.menu2
                self.params["category"] = menu[choice]
                break


    def menu2(self):
        """ this method is to show the menu of products
        for the client's interface """

        print("Dans self.params", self.params)
        
        menu = Menu(["product 1", "product 2", "product 3", "product 4"])

        while True:
            print(menu)
            choice = input(">>>  ")

            if menu.is_valid_choice(choice):
                self.next  = self.menu3
                self.params["product"] = menu[choice]
                break


    def input(self, menu):
        """ this method handles the input from the user according
        to where he wants to navigate in the menu of the application """
        
        while True:

            print(menu)
            choice = input(">>>  ")

            if menu.is_valid_choice(choice):
                self.next  = self.menu3
                self.params["product"] = menu[choice]
                break



    def menu3(self):
        """ THis method is to show the menu of substitutes products
        for the client's interface """

        print("Dans self.params", self.params)

        menu = Menu(["substitute 1", "substitute 2", "substitute 3", "substitute 4"])

        while True:
            print(menu)
            choice = input(">>>  ")

            if menu.is_valid_choice(choice):
                self.next  = self.quit
                self.params["substitute"] = menu[choice]
                break


    def quit(self): 
        """ This method manages the option quit 
        from the menu for the client's interface """

        print("Dans self.params", self.params)
        self.running = False
        print("Good Bye")



client = Client()
client.start()
