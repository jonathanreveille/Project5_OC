#! /usr/bin/env python3
# coding : utf-8


class Product:
    """ This class contains all information about product """

    def __init__(self, code, url, product_name, stores, brands, nutrition_grade_fr, description, category, **kwargs):
        
        self.code = code
        self.name = product_name
        self.description = description
        self.url = url
        self.brands = brands
        self.nutrition_grade = nutrition_grade_fr
        self.category = category
        # Table association ?
        self.stores = []

        for category in category.split(","):
            self.stores.append(Category(category.name.lower().strip()))

        for store in stores.split(","):
            self.stores.append(Store(store.name.lower().strip()))

    def __repr__(self):
        return f"Product(name: {self.name})"


class Store: 
    """ This class contains all information 
    about stores """

    def __init__(self, store):
        self.name = store

    def __repr__(self):
        f"Store (name: {self.name})"


class Category:
    """ This class contains all the information 
    about Categories """

    def __init__(self, category):
        self.name = category

    def __repr__(self):
        f"Category (name: {self.name})"


class Brand:
    """ This class contains all the information 
    about the Brands"""

    def __init__(self, brand):
        self.name = brand

    def __repr__(self):
        f"Brand(name: {self.name})"


