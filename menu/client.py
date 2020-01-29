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
                    self.next = self.menu7

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

        for product in self.product_manager.get_unhealthy_products(self.params["category"]):
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

        # print("Dans self.params", self.params)

        for product in self.product_manager.get_healthy_products(self.params["category"]):
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
        """this method shows the user addition data about the substituted
        product."""

        # print("Dans self.params", self.params)

        print("PLEASE FIND ADDITIONAL DATA ABOUT THE SELECTED PRODUCT")
        print("(sometimes, product from different brands have the same product name) : ")

        for product in self.product_manager.get_data_from_substitute(self.params["substitute"]):
            print(" -  ", product.product_name.capitalize(), '>>> nutriscore : ', product.nutrition_grade_fr.upper(), "--",
                  product.brand.brand_name,"-- more data :", product.url)

        menu = Menu(["WHERE TO BUY IT ?"])

        while True:
            print(menu)
            choice = input(">> ")

            if menu.is_valid_choice(choice):
                entry = menu[choice]
                self.params["Where to buy"] = entry
                self.next = self.menu5

                if entry == "QUIT":
                    self.next = self.quit_app

                elif entry == "HOME":
                    self.next = self.back_home

            break

    def menu5(self):
        """This method shows the store where we can buy the product."""

        self.stores = []

        for store in self.product_manager.get_store_name_for_product(self.params["substitute"]):
            self.stores.append(store)
            print("Store : ", store.store_name.capitalize())

        menu = Menu(["ADD TO FAVORITES ?"])

        while True:
            print(menu)
            choice = input(">> ")

            if menu.is_valid_choice(choice):
                entry = menu[choice]
                # self.params["favorite"] = entry
                self.next = self.menu6

                if entry == "QUIT":
                    self.next = self.quit_app

                elif entry == "HOME":
                    self.next = self.back_home

            break

    def menu6(self):
        """this method is the menu where all favorite products were saved by
        the user."""

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
                self.next = self.menu7

                if entry == "QUIT":
                    self.next = self.quit_app

                elif entry == "HOME":
                    self.next = self.back_home

            break

    def menu7(self):
        """This menu shows all the products that have been 
        saved by the user"""

        menu = Menu([])

        while True:

            for favorite in self.favorite_manager.show_favorites():

                print(
                    f" -  {favorite.substitute_products.product_name}, ({favorite.substitute_products.nutrition_grade_fr.upper()})")
                print(
                    f"    Brand : {favorite.substitute_products.brand.brand_name}")
                print(f"    URL : {favorite.substitute_products.url}")
                print(f"    Stores : ", end="")

                stores = []

                for store in self.product_manager.get_store_name_for_product(favorite.substitute_products.product_name):
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
