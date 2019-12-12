#! /usr/bin/env python3
# coding : utf-8


class Product:
    """ This class contains all information about product """

    def __init__(self, code, url, product_name, stores, brands, nutrition_grade_fr, description, **kwargs):
        
        self.code = code
        self.name = product_name
        self.description = description
        self.url = url
        self.brands = brands
        self.nutrition_grade = nutrition_grade_fr
        # Table association ?
        self.stores = []

        for store in stores.split(","):
            self.stores.append(Store(store.name.lower().strip()))

    def __repr__(self):
        return f"Product name:({self.name})"


class Store: 
    """ This class contains all information 
    about stores """

    def __init__(self, store):
        self.name = store

    def __repr__(self):
        f"Store (name :{self.name})"


class Category:
    """ This class contains all the information 
    about Categories """

    def __init__(self, category):
        self.name_cat = category


class Brand:
    """ This class contains all the information 
    about Categories """

    def __init__(self, brand):
        self.name_brand = brand


