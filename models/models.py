#! /usr/bin/env python3
# coding : utf-8


class Product:
    """ This class contains all information about product """

    def __init__(self, code, url, product_name, stores, brands, nutrition_grade_fr, ingredients, categories, **kwargs):
        
        self.code = code
        self.name = product_name
        self.url = url
        self.brands = brands
        self.nutrition_grade = nutrition_grade_fr
        self.category = []
        self.ingredients = ingredients
        # Table association ProductStore?
        self.stores = []

        for store in stores.split(","):
            self.stores.append(Store(store.lower().strip()))
        
        for category in categories.split(","):
            self.category.append(Category(category.lower().strip()))

    def __repr__(self):
        return f"Product(name: {self.name})"


    def is_valid(self, product, **kwargs):
        """ This method is to check if our list has all the data entries we need to create our objects """

        is_valid = True

        parameters = ("product_name","nutrition_grade_fr",\
                "categories", "code", "stores", "brands",\
                "code", "url")

        for parameter in parameters:
        
            if parameter not in product or not product[parameter]:# We check if we have the corresponding keys (parameters) in dict
                is_valid = False
                break

            if not product[parameter]:  # On vérifie que ça contient un truc
                is_valid = False
                break

        return is_valid


    # for parameter in parameters:
    #     if parameter not in product or not product[parameter]:
    #         not_valid_products.append(product)
    #         print("-->DEBUGGING", product.get('product_name'), f"{parameter} not present or empty")
    #         return False
    #     else:
    #         return True


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


def main():
    pass

if __name__ == "__main__":
    pass