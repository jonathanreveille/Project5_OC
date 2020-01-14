import peewee

from .models import Category, Product, Store, Brand, Favorite, ProductStore


""" this module will have the responsibility 
to be able to search through our data """


class ProductManager:

    def __init__(self):
        self.query = None
    

    def show_all_products_from_db(self):
        """ this method is to access all product name from  db """

        for product in Product.select():
            print(product.product_name)

    def show_all_category(self):
        """ this method is to get all categories in db"""

        for category in Category.select():
            print(category.category_name)


    def get_products_from_category(self):
        """ get in return name of products associated to the
        selected category """
        pass

        # for products in Product.select().join(Category).where(Category.category_name=="biscuits"):
        #     print(products.category)


    def get_healthy_product(self):
        """ get all products from one category
        ordered by nutriscore (best to worst)"""
        pass


    def get_unhealthy_product(self):
        """ get all products from one category
        ordered by nutriscore (worst to best)"""
        pass


    def get_store_for_product(self):
        """ get name of stores where 
        we can buy a product """
        pass


    def add_to_favorites(self):
        """ this method will join a product to 
        replace by an healthier choice """
        pass


if __name__ == "__main__":

    productmanager = ProductManager()
    productmanager.show_all_products_from_db()
    productmanager.get_products_from_category()





        #query =  Product.category.select()
        # query =  Product.select(Product.product_name)

        # for row in query:
        #     print(row)
