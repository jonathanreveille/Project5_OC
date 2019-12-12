#! /usr/bin/env python3
# coding : utf-8

class Product:
    """ class that contains product information """

    def __init__(self, **product):
        
        self.code = product["code"]
        self.url_name = product["url_name"]
        self.product_name_fr = product["product_name_fr"]
        self.stores = product["stores"]
        self.brands = product["brands"]
        self.nutrition_grade = product["nutrition_grade_fr"]
        self.has_palm_oil = product["ingredients_that_may_be_from_palm_oil_tags"]
        self.description = product["description"]


    def __repr__(self):
        return f"Product({self.product_name_fr}, from {self.brands} can be found in {self.stores})"



class ProductManager:
    """ this class allows us to manipulate products"""
    def __init__(self):
        pass

    def get_or_create(self):
        """ this method is to add a new lines into our database tables """

    def save(self):
        """ this method is to save a new line for our database tables """
        pass

    def get_by_name(self):
        """ this method is to search for a product by its name """