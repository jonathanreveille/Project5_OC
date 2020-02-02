#! /usr/bin/env python3
# coding : utf-8

from .menu import MenuHome, Menu

from bdd.productmanager import ProductManager
from bdd.favoritemanager import FavoriteManager


class Client:

    def __init__(self):

        self.running = False  # acts like a switch  ON/OFF
        self.next = self.menu0
        self.params = {}

        self.product_manager = ProductManager()
        self.product_list = list()

        self.category_list = list()
        self.substitute_list = list()
        self.store = list()

        self.favorite_manager = FavoriteManager()
        self.favorite_list = list()

    def start(self):
        """This method is the loop  to  make the application launch."""

        self.running = True  # the switch is turned ON

        while self.running:
            # print("DEBUG:", self.next.__name__)
            self.next()
            # points toward the method menu0, defined in attributes

    def menu0(self):
        """This menu will ask user what he wishes to do on the application."""
        # print("Dans self.params: ", self.params)
        print("WELCOME TO PUR-BEURRE, WHAT DO YOU WISH TO DO TODAY ?")

        menu = MenuHome(["Find an healthier product ?",
                         "Go to favorites"])

        while True:
            print(menu)
            choice = input(">>>  ")

            if menu.is_valid_choice(choice):
                self.next = self.menu1
                entry = menu[choice]
                self.params["action"] = menu[choice]

                if entry == "Go to favorites":
                    self.next = self.menu6

                elif entry == "QUIT":
                    self.next = self.quit_app

                elif entry == "HOME":
                    self.next = self.back_home

            break

    def menu1(self):  # CATEGORY MENU
        """this method shows all the present categories to the user in this
        menu."""

        for category in self.product_manager.get_all_category():
            self.category_list.append(category.category_name.capitalize())

        menu = Menu(self.category_list)

        while True:

            print("CHOOSE A CATEGORY : ")
            print(menu)

            choice = input(">>>  ")
            if menu.is_valid_choice(choice):
                self.next = self.menu2
                entry = menu[choice]
                self.params["category"] = entry

                if entry == "QUIT":
                    self.next = self.quit_app

                elif entry == "HOME":
                    self.next = self.back_home

            break

    def menu2(self):  # UNHEALTHY PRODUCT MENU
        """This method shows the menu of products for the user."""

        # print("Dans self.params", self.params)

        for product in (
            (self.product_manager.get_unhealthy_products(
                self.params["category"])
             )):
            self.product_list.append(product.product_name)

        menu = Menu(self.product_list)

        while True:

            print("CHOOSE A PRODUCT THAT YOU MIGHT KNOW :")
            print(menu)
            choice = input(">>>  ")

            if menu.is_valid_choice(choice):
                self.next = self.menu3
                entry = menu[choice]
                self.params["product"] = entry

                if entry == "QUIT":
                    self.next = self.quit_app

                elif entry == "HOME":
                    self.next = self.back_home

            break

    def menu3(self):
        """This method is to show the menu of substitutes
        products for the user."""

        for product in self.product_manager.get_healthy_products(
            self.params["category"]
        ):
            self.substitute_list.append(product.product_name)

        menu = Menu(self.substitute_list)

        while True:

            print("CHOOSE A PRODUCT THAT WILL REPLACE IT :")
            print(menu)
            choice = input(">>>  ")

            if menu.is_valid_choice(choice):
                self.next = self.menu4
                entry = menu[choice]
                self.params["substitute"] = entry

                if entry == "QUIT":
                    self.next = self.quit_app

                elif entry == "HOME":
                    self.next = self.back_home

            break

    def menu4(self):
        """This method ask if the user wants to add
        to favorite the product he selected from
        the healthy list of products"""

        print("Dans self.params: ", self.params)

        menu = Menu(["ADD TO FAVORITES?"])

        while True:
            print(menu)
            choice = input(">> ")

            if menu.is_valid_choice(choice):
                entry = menu[choice]
                self.next = self.menu5

                if entry == "QUIT":
                    self.next = self.quit_app

                elif entry == "HOME":
                    self.next = self.back_home

            break

    def menu5(self):
        """This method warns the user that his search has been
        saved to his favorites, and it asks him if he wants to
        go his favorite menu."""

        print("Dans self.params: ", self.params)

        self.original = self.params["product"]
        self.substitute = self.params["substitute"]

        self.favorite_manager.save_to_favorites(self.original, self.substitute)

        menu = Menu(["GO TO FAVORITES"])

        while True:

            print("Your product has been saved to your favorites")
            print(menu)
            choice = input(">>  ")

            if menu.is_valid_choice(choice):
                entry = menu[choice]
                self.params["favorite"] = entry
                self.next = self.menu6

                if entry == "QUIT":
                    self.next = self.quit_app

                elif entry == "HOME":
                    self.next = self.back_home

            break

    def menu6(self):
        """This menu shows all the products that have been
        saved to Favorites by the user"""

        menu = Menu([])

        while True:

            for fav in self.favorite_manager.show_favorites():

                print(
                    f" -  {fav.substitute_products.product_name},"
                    f"({fav.substitute_products.nutrition_grade_fr.upper()})"
                )
                print(
                    f"    Brand : "
                    f"{fav.substitute_products.brand.brand_name.capitalize()}"
                )
                print(
                    f"    URL : {fav.substitute_products.url}"
                )

                print(f"    Stores : ", end="")

                stores = []

                for store in self.product_manager.get_store_name_for_product(
                    fav.substitute_products.product_name
                ):
                    stores.append(store.store_name.upper())

                print(", ".join(stores))

            print(menu)
            choice = input(">>  ")

            if menu.is_valid_choice(choice):
                entry = menu[choice]

                if entry == "QUIT":
                    self.next = self.quit_app

                elif entry == "HOME":
                    self.next = self.back_home

            break

    def back_home(self):
        """this method is to get back at the main menu deleting all other past
        search from user's session."""

        # print("Dans self.params", self.params)

        self.running = True
        self.next = self.menu0
        self.params = {}
        self.category_list = []
        self.product_list = []
        self.substitute_list = []
        self.favorite_list = []

    def quit_app(self):
        """This method manages the option quit 1 from the menu for the client's
        interface."""

        # print("Dans self.params", self.params)

        quit_yes_or_no = input(">>> Do you really want to QUIT ? Y / N :  ")

        if quit_yes_or_no == "Y":
            self.running = False
            print("Good Bye, see you another time ")

        elif quit_yes_or_no == "N":
            self.running = True
            self.next = self.back_home


client = Client()
client.start()
