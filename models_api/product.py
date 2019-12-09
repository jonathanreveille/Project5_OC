#! /usr/bin/env python3
# coding : utf-8

from settings.settings import KEYWORDS


class Product:
    """ class that contains product information """

    def __init__(self, **article):
        self.product_name_fr = article["product_name_fr"]
        self.stores = article["store"]
        self.nutrition_grade = article["nutrition_grade_fr"]
        self.id = article["id"]
        self.brand = article["brands"]


    def __repr__(self):
        return f"Product({self.product_name_fr})"


    @classmethod
    def is_valid(cls, article):
        """ Method that checks if all data
        needed are attached to our product """

        is_valid = True

        for word in list(KEYWORDS):

            if word not in article:
                is_valid = False
                break

            if not article[word]:
                is_valid = False
                break

        return is_valid



        


        

