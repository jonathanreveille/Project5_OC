#! /usr/bin/env python3
# coding : utf-8

import peewee

from .models import Favorite, Product


    class FavoriteManager():
        """ this class handles the favorites of the user """


        def __init__(self):
            self.original = str()
            self.substitute = str()
            self.list_to_add_to_favorite = list()


        def __str__(self):
            """returns a string of our object """

            return f"the original product is {self.original} is replaced by: {self.substitute}"


        def save_to_favorites(self, original, substitute):
            """ this method will join a product to 
            replace by an healthier choice """

            self.original = original
            self.substitute = substitute

            self.list_to_add_to_favorite.append((self.original, self.substitute))

            for original, substitutes in self.list_to_add_to_favorite:
                product_obj = Product.get(Product.product_name == self.original)

                for substitute in substitutes:
                    sub_obj = Product.get(Product.product_name == self.substitute)
                    Favorite.create(substituted_product = product_obj, substitute_products = sub_obj)



    def show_favorite(self):
        """ this method is to access all product favorited from db """
        
        return list(Favorite.select(Favorite.substitute_products, Favorite.substituted_product))


    def delete_from_favorite(self, to_delete):

        self.line_to_delete = to_delete

        (Favorite.delete()
        .where((Favorite.substitute_product)
            & (Favorite.substituted_products)).execute())

            #NOT TOO SURE ABOUT THAT ^^^^





        #self.list_to_add_to_favorite.append((self.original, self.substitute))

        #Favorite.create(substituted_product = self.original, substitute_products = self.substitute)

        # self.list_to_add_to_favorite.append((self.substitute, self.original))

        # for product in self.original:
        #     Product.get(Product.product_name == product)
        #     for substitute in self.substitute:
        #         Product.get(Product.product_name == substitute)
        #         Favorite.create(substituted_product = original, substitute_products = substitute)



        # for original, substitutes in self.list_to_add_to_favorite:

        #     original = Product.get(Product.product_name == original)

        #     for substitute in substitutes:
        #         sub_prod = Product.get(Product.product_name == sub_prod)
        #         Favorite.create(substituted_product = original, substitute_products = substitute)

        # favorite, created = Favorite.get(
        #     substituted_product = self.original,
        #     substitute_products = self.substitute)


#   for username, favorites in favorite_data:
#         user = User.get(User.username == username)
#         for content in favorites:
#             tweet = Tweet.get(Tweet.content == content)
#             Favorite.create(user=user, tweet=tweet)
