#! /usr/bin/env python3
# coding : utf-8

import peewee

from .models import Favorite


class FavoriteManager():


    def __init__(self, substitute, original):
        self.substitute = substitute
        self.original = original


    def insert_to_favorites(self):
        """ this method will join a product to 
        replace by an healthier choice """
        
        print("Do you want to save this new product to your favorite list")
        save_to_favorite = input(">>> YES or NO ? ")

        if save_to_favorite == "YES":
            Favorite.create()

            #WORKING HERE NOW


    def delete_from_favorite(self):
        pass


    def update_favorite(self):
        pass
    