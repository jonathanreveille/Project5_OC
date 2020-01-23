#! /usr/bin/env python3
# coding : utf-8

import peewee

from .models import Favorite, Product


class FavoriteManager():
    """ this class handles the favorites of the user """


    def __init__(self):
        self.original = list()
        self.substitute = list()
        self.favorites = list()


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
        """ this method will retrieve data from Favorite table
        into the name of products for the user's favorite list"""

        


        # for favorite in (
        #     Favorite.select()
        # .join(
        #     (Product, join_type = JOIN.LEFT_OUTER, on=(favorite.substituted_product == Product.product_name))
        # )):

        #     print(product.product_name, product.product_name) 


        # for product in (
        #     Product.select(Product, Favorite)
        # .join(Favorite.substituted_product, Favorite.substitute_products)
        # .where(
        #     (product.product_name == Favorite.substituted_product)
        #     &(product.product_name == Favorite.substitute_products))):

        #     print(product.product_name, product.product_name)


        # for product in (
        #     Product.select(Product, Favorite)
        # .join(Favorite.substituted_product, Favorite.substitute_products)
        # .where(
        #     (Favorite.substituted_product == Product.product_name)
        #     &(Favorite.substitute_products == Product.product_name))):

        #     print(product.product_name, product.product_name)

        #>>>Traceback (most recent call last):
#   File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/runpy.py", line 193, in _run_module_as_main
#     "__main__", mod_spec)
#   File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/runpy.py", line 85, in _run_code
#     exec(code, run_globals)
#   File "/Users/jonathanreveille/dev/librequest/bdd/favoritemanager.py", line 82, in <module>
#     favorite_manager.show_favorites()
#   File "/Users/jonathanreveille/dev/librequest/bdd/favoritemanager.py", line 50, in show_favorites
#     (Favorite.substituted_product == product.product_name)
# UnboundLocalError: local variable 'product' referenced before assignment




        # for favorite in (Favorite.select()
        #     .join(Product)
        #     .join(Favorite)
        #     .where(
        #         (favorite.substituted_product = Product.product_name)
        #     &(favorite.substitute_products = Product.product_name)
        #     )):

        #     print(favorite.substituted_product, ">> replaced by >>", favorite.substitute_products)

    
    def delete_from_favorite(self, to_delete):

        self.line_to_delete = to_delete

        (Favorite.delete()
        .where((Favorite.substitute_product)
            & (Favorite.substituted_products)).execute())

            #NOT TOO SURE ABOUT THAT ^^^^




favorite_manager = FavoriteManager()
favorite_manager.show_favorites()



 # def save_to_favorites(self, original, substitute): # BEFORE EDITING
    #     """ this method will join a product to  
    #     replace by an healthier choice """

    #     self.original = original
    #     self.substitute = substitute

    #     self.list_to_add_to_favorite.append((self.original, self.substitute))

    #     for original, substitutes in self.list_to_add_to_favorite:
    #         product_obj = Product.get(Product.product_name == self.original)

    #         for substitute in substitutes:
    #             sub_obj = Product.get(Product.product_name == self.substitute)
    #             Favorite.create(substituted_product = product_obj, substitute_products = sub_obj)
        
    #     og = Product.select(Product.product_name == self.original)
    #     re = Product.select(Product.product_name == self.substitute)
    #     Favorite.get(substituted_product = og, substitute_products = re)

    #    # Favorite.get_or_create(substitute_products = self.substitute)


       

    # def show_favorites(self):
    #     """ this method is to access all product favorited from db """
        
    #     for favorite in (
    #         Favorite.select()
    #         .join(Favorite, JOIN.NATURAL)
    #         .join(Product, JOIN.NATURAL)
    #         .where(favorite.substituted_product == Product.product_name)&
    #         (favorite.substitute_products == Product.product_name)
    #         ):

    #         print(favorite.substituted_product, favorite.substitute_product)
    #         #print(product.product_name, product.product_name)



        # return list(Store.select()
        # .join(ProductStore)
        # .join(Product)
        # .where(Product.product_name == self.query))

        # return list(Favorite.select(Favorite.substitute_products, Favorite.substituted_product))
        # for favorite in (Favorite.select()
        # .join(Product)
        # .join(Favorite)
        # .where(Favorite.substituted_product == Product.product_name)&(Favorite.substitue_products == Product.product_name)):
            
        #     print(favorite.substitute_products, favorite.substituted_product)

        
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
