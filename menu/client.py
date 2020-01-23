#! /usr/bin/env python3
# coding : utf-8

import os
import time

from .menu import Menu
from bdd.productmanager import ProductManager
from bdd.favoritemanager import FavoriteManager


class Client:


    def __init__(self):
        self.running = False # acts like a switch  ON/OFF
        self.next  = self.menu0
        self.params = {}

        self.product_manager = ProductManager()
        self.product_list = list()

        self.category_list = list()
        self.substitute_list = list()
        self.store = list()

        self.favorite_manager = FavoriteManager()
        self.favorite_list = list()


    def start(self):
        """ This method is the loop  to  make the application launch """
        
        self.running = True # the switch is turned ON

        while self.running:

            self.next() #points toward the method menu0, defined in attributes


    def menu0(self):
        """ This menu will ask the user what he wishes to 
        do on the application """

        os.system('clear')

        # print("Dans self.params: ", self.params)
        print("WELCOME TO PUR-BEURRE, WHAT DO YOU WISH TO DO TODAY ?")
        
        menu = Menu(["Find an healthier product ?",
                    "Go to favorites"])

        while True:
            print(menu)
            choice = input(">>>  ")

            if menu.is_valid_choice(choice):
                self.next = self.menu1
                entry = menu[choice]
                self.params["action"] = menu[choice]

                if entry == "Go to favorites":
                    self.next == self.menu7

                if entry == "QUIT":
                    self.next = self.quit_app

                elif entry == "HOME":
                    self.next = self.back_home

            break


    def menu1(self): #CATEGORY MENU
        """ this method shows all the present categories
         to the user in this menu"""

        os.system('clear')

        for category in self.product_manager.get_all_category():
            self.category_list.append(category.category_name.capitalize())
        
        menu = Menu(self.category_list)

        while True:
            os.system('clear')
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


    def menu2(self): #UNHEALTHY PRODUCT MENU
        """ this method shows the menu of products
        for the user """

        os.system('clear')

        print("Dans self.params", self.params)

        for product in self.product_manager.get_unhealthy_products(self.params["category"]):
            self.product_list.append(product.product_name)

        menu = Menu(self.product_list)

        while True:
            os.system('clear')
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


    def menu3(self): #HEALTHY PRODUCT MENU
        """ THis method is to show the menu of substitutes products
        for the user """

        os.system('clear')

        print("Dans self.params", self.params)

        for product in self.product_manager.get_healthy_products(self.params["category"]):
            self.substitute_list.append(product.product_name)
           
        menu = Menu(self.substitute_list)

        while True:
            os.system('clear')
            print("CHOOSE A PRODUCT THAT WILL REPLACE IT :")
            print(menu)
            choice =  input(">>>  ")

            if menu.is_valid_choice(choice):
                self.next = self.menu4
                entry = menu[choice]
                self.params["substitute"] = entry

                if entry == "QUIT":
                    self.next = self.quit_app

                elif entry == "HOME":
                    self.next = self.back_home
            
            break


    def menu4(self): # more info about product ?
        """ this method shows the user addition data 
        about the substituted product """
        
        os.system('clear')

        #print("Dans self.params", self.params)

        print("PLEASE FIND ADDITIONAL DATA ABOUT THE PRODUCT SELECTED :  ")

        for product in self.product_manager.get_data_from_substitute(self.params["substitute"]):
            print(product.product_name.capitalize(), '>>> nutriscore : ', product.nutrition_grade_fr.upper(),"--",
                "more data :", product.url)

        menu = Menu(["WHERE TO BUY IT ?"])

        while True:
            print(menu)
            choice = input(">> ")

            if menu.is_valid_choice(choice):
                self.next = self.menu5

                if choice == "QUIT":
                    self.next = self.quit_app

                elif choice == "HOME":
                    self.next = self.back_home

            break



    def menu5(self):
        """ This method shows the store where we can 
        buy the product """
    
        os.system('clear')

        for store in self.product_manager.get_store_name_for_product(self.params["substitute"]):

            print("Here is the store where you can get it : ", store.store_name.capitalize())

        menu = Menu(["ADD TO FAVORITES ?"])

        while True:
            print(menu)
            choice = input(">> ")

            if menu.is_valid_choice(choice):
                entry = menu[choice]
                self.params["Add to favorite"] = entry
                self.next = self.menu6

                if entry == "QUIT":
                    self.next = self.quit_app

                elif entry == "HOME":
                    self.next = self.back_home

            break


    def menu6(self):
        """ this method is the menu where all favorite products
        were saved by the user """

        self.original = self.params["product"]
        self.substitute = self.params["substitute"]

        self.favorite_manager.save_to_favorites(self.original, self.substitute)

        menu = Menu(["See your list of favorites"])

        while True:

            print("Your product has been saved to your favorites")
            print(menu)
            choice = input(">>  ")
            if menu.is_valid_choice(choice):
                self.next = self.menu7

                if choice == "QUIT":
                    self.next = self.quit_app

                elif choice == "HOME":
                    self.next = self.back_home

            break


    def menu7(self): # I dont want these brakets... need to find a solution
        """ this menu shows all the products that have been saved by the user """

        for favorite in self.favorite_manager.show_favorites():

            self.favorite_list.append(
                (favorite.substituted_product.product_name,
                favorite.substitute_products.brand.brand_name,
                favorite.substitute_products.nutrition_grade_fr,
                favorite.substitute_products.url))
           
            # print(
            #     favorite.substituted_product.product_name,
            #     ">> replaced by :", favorite.substitute_products.product_name, 
            #     "-- nutriscore :", favorite.substitute_products.nutrition_grade_fr.upper(),
            #     "-- brand :", favorite.substitute_products.brand.brand_name,
            #     " -- find more data : ", favorite.substitute_products.url)

        menu = Menu(self.favorite_list)


        while True:
            print("Here is your favorite list of products")
            print(menu)
            choice = input(">>  ")
            if menu.is_valid_choice(choice):
                self.next = self.back_home
                
                if choice == "QUIT":
                    self.next = self.quit_app

                elif choice == "HOME":
                    self.next = self.back_home

            break



    def back_home(self):
        """ this method is to get back at the main menu
        deleting all other past search from user's session"""

        print("Dans self.params", self.params)

        back_home = input(">> Are you sure you want to go back HOME ? Y / N : ")

        if back_home == "Y":
            self.running = True
            self.next = self.menu0
            self.params = {}
            self.category_list = []
            self.product_list= []
            self.substitute_list = []
            self.favorite_list = []

        else:
            pass



    def quit_app(self): 
        """ This method manages the option quit 1
        from the menu for the client's interface """

        print("Dans self.params", self.params)

        quit_yes_or_no = input(">>> Do you really want to QUIT ? Y / N :  ")
        
        if quit_yes_or_no == "Y":
            self.running = False
            print("Good Bye, see you another time ")
            time.sleep(3)
            

        elif quit_yes_or_no  ==  "N":
            self.running = True 
            self.next = self.back_home


client = Client()
client.start()

    # def menu4(self): # ADD THIS PRODUCT TO YOUR FAVORITES ?
    #     """ this method will ask the user if he wants to 
    #     save his search into his favorites """

    #     print("Votre recherche :", self.params)

    #     print("Voulez-vous savoir où acheter de produit?")

    #     menu = Menu(["Oui, je veux savoir dans quel magasin l'acheter ?"])

    #     while True:

    #         print(menu)
    #         choice =  input(">>>  ")

    #         if menu.is_valid_choice(choice):
    #             self.next = self.menu_store
    #             entry = menu[choice]
    #             self.params["add_favorite"] = entry

    #             if entry == "QUIT":
    #                 self.next = self.quit_app

    #             elif entry == "HOME":
    #                 self.next = self.back_home
        
    #         break


    # def menu_store(self):
    #     """ this method is to get all the stores from a product """
        
    #     for store in self.product_manager.get_store_name_for_product(self.params["substitute"]):
    #         self.store.append(store.store_name)

    #     menu = Menu(self.store)

    #     while True:

    #         print(menu)

    #         choice =  input(">>> ")
            
    #         if menu.is_valid_choice(choice):
    #             self.next = self.menu_store
    #             entry = menu[choice]
    #             self.params["add_favorite"] = entry

    #             if choice == "Y":
    #                 self.next = self.menu_data

    #             elif choice  ==  "N":
    #                 self.next = self.menu_favorite #instead of menu0

    #             if choice == "QUIT":
    #                 self.next = self.quit_app

    #             elif choice == "HOME":
    #                 self.next = self.back_home
            
    #         break
    

    # def menu_data(self):
    #     """ this method gives the user the access 
    #     to more data about the seeked product"""


    #     for product in self.product_manager.get_data_from_substitute(self.params["substitute"]):
    #         self.additional_data.append(product.product_name, product.nutrition_grade_fr, product.url)

    #     print(self.additional_data)







        # for store in self.product_manager.get_store_name_for_product(self.params["substitute"]):
        #     self.store.append(store.store_name)

        #     print(self.store)

        #     break

#BROUILLON:

        # self.category = list()
        # self.product = list()
        # self.substitute = list()
        # ce sera pour les stores ça
        #for store in self.product_manager.get_store_from_product():
            #print(Store.store_name)


    # def build_menu_category(self):

    #     for category in self.product_manager.get_all_category():
    #         self.category.append(category)
    #         return list(self.category)
