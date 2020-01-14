#! /usr/bin/env python3
# coding : utf-8

# categories = ["cat1", "cat2", "cat3"]

# x = "___".join(categories)
# print(x)
# # result >>> cat1___cat2___cat3

# y = "/n".join(categories)
# print(y)
# # result >>> cat1/ncat2/ncat3


from .menu import Menu

class Client:

    def __init__(self):
        self.running = False # acts like a switch  ON/OFF
        self.next  = self.menu0
        self.params = {}


    def start(self):
        """ this method is the loop  to  make the application launch """
        
        self.running = True

        while self.running:
            self.next()


    def menu0(self):
        """ This menu will ask the user what he wishes to 
        do on the application """

        print("Dans self.params: ", self.params)
        
        menu = Menu(["Rechercher un produit", "Voir liste de favoris"])

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
        
        while  True:
            print(menu)
            choice =  input(">>>  ")

            if menu.is_valid_choice(choice):
                self.next = self.menu2
                entry = menu[choice]
                
                self.params["category"] = entry

                if entry == "QUIT":
                    self.next = self.quit

                elif entry == "HOME":
                    self.next = self.menu0

            break

    def input_choice_from_user(self, menu):
        """ this method manages the input of the user to allow
        him to navigate through the application """

        while True:

            print(menu)
            choice =  input(">>>  ")

            if menu.is_valid_choice(choice):
                self.next = self.menu2
                entry = menu[choice]
                self.params["category"] = entry

                if entry == "QUIT":
                    self.next = self.quit

                elif entry == "HOME":
                    self.next = self.menu0

            break


    def menu2(self):
        """ this method is to show the menu of products
        for the client's interface """

        print("Dans self.params", self.params)
        
        menu = Menu(["product 1", "product 2", "product 3", "product 4", "HOME", "QUIT"])

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

        menu = Menu(["substitute 1", "substitute 2", "substitute 3", "substitute 4", "HOME", "QUIT"])

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


    def input_choice(self, menu):
        """ this method handles the input from the user according
        to where he wants to navigate in the menu of the application """
        
        while True:

            print(menu)
            choice = input(">>>  ")

            if menu.is_valid_choice(choice):
                if choice == "quit":
                    self.next == self.quit

                elif choice == "home":
                    self.next = self.menu1
                else:
                    self.next = menu[choice]

            break


client = Client()
client.start()
