#! /usr/bin/env python3
# coding : utf-8

from peewee import fn

from .models import Category, Product, Store, Brand, ProductStore

""" this module will have the responsibility 
to be able to search through our data """

class ProductManager:

    def __init__(self):
        self.query = []


    def get_all_products_from_db(self):
        """ this method is to access all product name from  db """
        
        for product in (
            Product.select()
            .order_by(fn.Rand())
            .limit(10)
            ): # get randomly 10 products from the db
            
            print(product.product_name)


    def get_all_category(self):
        """ this method is to get all categories from the database """

        return list(Category.select())


    def get_products_from_category(self, category):
        """ This method is to get all products from a category """

        self.query = category

        return list(Product.select()
        .join(Category)
        .where(Category.category_name == self.query)
        .order_by(fn.Rand()).limit(10))

    
    def get_unhealthy_products(self, category):
        """ this method is to get all unhealthy product from a category
        from the database """

        self.query = category 

        return list(Product
                .select(Product.product_name, Product.category, Product.nutrition_grade_fr)
                .join(Category)
                .where(
                    (Category.category_name == self.query)
                    & (Product.nutrition_grade_fr >= "c")
                )
                .order_by(fn.Rand()).limit(10)
            )


    def get_healthy_products(self, category):
        """ this method is to get all healthy product from a category
        from the database """

        self.query = category 

        return list(Product
                .select(Product.product_name, Product.category, Product.nutrition_grade_fr)
                .join(Category)
                .where(
                    (Category.category_name == self.query) \
                    & (Product.nutrition_grade_fr <= "b"))
                .order_by(fn.Rand()).limit(10))


    def get_store_name_for_product(self, product):
        """ get name of stores where we can buy a product """

        self.query == product

        return list(Store.select()
        .join(ProductStore)
        .join(Product)
        .where(Product.product_name == self.query))


    def get_data_from_substitute(self, product):
        """ this method is to get all the additionnal information about a product 
        that the user selects to save to his favorites """

        self.query = product

        return list(Product.select()
        .where(Product.product_name == self.query)
        .order_by(Product.product_name).limit(10))
