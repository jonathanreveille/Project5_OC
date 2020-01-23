#! /usr/bin/env python3
# coding : utf-8

import peewee
from peewee import JOIN

from .models import Favorite, Product


class FavoriteManager():
    """ this class handles the favorites of the user """


    def __init__(self):
        self.original = list()
        self.substitute = list()
        self.favorites = list()
        # self.delete_from_favorite = str()


    def __str__(self):
        """returns a string of our object """

        return f"the original product is {self.original} is replaced by: {self.substitute}"


    def save_to_favorites(self, original, substitute):
        """ this method will join a product to 
        replace by an healthier choice """

        self.original = original
        self.substitute = substitute

        self.favorites.append((self.original, self.substitute))

        for original, substitutes in self.favorites:
            product_obj = Product.get(Product.product_name == self.original)

            for substitute in substitutes:
                sub_obj = Product.get(Product.product_name == self.substitute)
                Favorite.get_or_create(substituted_product = product_obj, substitute_products = sub_obj)


    def show_favorites(self):
        """ this method shows the foreign keys of products that
        has been saved into the user's favorite table """

        return list(Favorite.select())


    # def show_favorites2(self): #WORKS WELL
        # """ this method shows the foreign keys of products that
        # has been saved into the user's favorite table """

        # for favorite in Favorite.select():
        #     print(
        #         favorite.substituted_product.product_name, ">> replaced by :",
        #         favorite.substitute_products.product_name, "-- brand :", favorite.substitute_products.brand.brand_name,
        #         " -- find more data : ", favorite.substitute_products.url)


    def delete_from_favorite(self, to_delete):

        """ this method allows the user to delete 
        a line of his favorite product saved """

        #Working here
        pass

        self.line_to_delete = to_delete


# favorite_manager = FavoriteManager()
# favorite_manager.show_favorites()