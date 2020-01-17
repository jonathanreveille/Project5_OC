#! /usr/bin/env python3
# coding : utf-8

from peewee import fn

from .models import Category, Product, Store, Brand, ProductStore

""" this module will have the responsibility 
to be able to search through our data """

class ProductManager:

    def __init__(self):
        self.query = []
        #self.category = None #self.category = category # and add category into instance of class object
    

    def get_all_products_from_db(self):
        """ this method is to access all product name from  db """
        
        return list(Product.select().order_by(fn.Rand().limit(10)))

        #for product in [Product.select()]:
            #print(product.product_name)


    def get_category(self):
        """ this method is to get all categories from the database """

        return list(Category.select())

            #print(Category.category_name)


    def get_products_from_category(self, category):
        """ This method is to get all products from a category """

        return list(Product.select().join(Category).where(Category.category_name == self.query))

        # for product in Product.select().join(Category).where(Category.category_name == self.query):
        #     print(product.product_name)


    def get_healthy_products_from_category(self, category):
        """ This method  shows  all healthy product from the selected
        category (from best to worst) """

        self.query = category

        return list(Product.select().join(Category) \
        .where(Category.category_name == self.query) \
        .order_by(Product.nutrition_grade_fr)
        )

            #print(product.product_name, product.nutrition_grade_fr)


    def get_unhealthy_product_from_category(self, category):
        """ This method gets all products from one category
        ordered by its nutriscore (from worst to best)"""

        self.query = category

        return list(Product.select().join(Category) \
        .where(Category.category_name == self.query)
        .order_by(Product.nutrition_grade_fr.desc())
        )

           # print(product.product_name, product.nutrition_grade_fr)



    def get_store_name_from_product(self, product):
        """ get name of stores where we can buy a product """

        self.query = product

        return list(Store.select().join(ProductStore).join(Product).where(Product.product_name == self.query))

            # print(store.store_name)



productmanager = ProductManager()
productmanager.get_all_products_from_db()
productmanager.get_healthy_products_from_category("Pizza") # works
productmanager.get_unhealthy_product_from_category("Pizza") #works
productmanager.get_store_name_from_product("Pizza Kebab") # works >>> Auchan


#productmanager.get_healthy_product_from_category("Pizza") #works but show all the product


#productmanager.get_store_name() # still need to work on it
 

#productmanager.get_all_products_from_db() #works
#productmanager.get_products_from_category("Biscuits") #works

#productmanager.show_products_from_category("Pizza") #works
#productmanager.get_store_name() # works





    # WORKS but it shows all products from database : 
    # def get_healthy_product_from_category(self, category):
    #     """ get all products from one category
    #     ordered by nutriscore (best to worst)"""
        
    #     for product in Product.select().order_by(Product.nutrition_grade_fr):
    #         print(product.product_name, product.nutrition_grade_fr)

        #for pet in Pet.select().where(Pet.owner == uncle_bob).order_by(Pet.name):



     #for product in Product.select().join(Category).where(Category.category_name == "biscuits"): # IT WORKS
        #for product in Product.select().join(Category).where(Category.category_name == category):  #Factorize


        # for product in Product.select().join(Store).where(Store.store_name == "carrefour"):
        #     print(product.product_name)
        # >>> peewee.InternalError: (1054, "Unknown column 't3.store_name' in 'where clause'")



        # for store in Store.select():
        #     print(store.store_name)

        # query = Product.select().order_by(Product.product_name).prefetch(Store)

        # for product in query:
        #     print(product.product_name)
        #     for store in product.store:
        #         print('  *', store.store_name)




    #productmanager.show_all_category()
    #productmanager.get_products_from_category('Biscuits')





        #query =  Product.category.select()
        # query =  Product.select(Product.product_name)

        # for row in query:
        #     print(row)


    # def show_all_category(self):
    #     """ this method is to get all categories in db"""

    #     for category in Category.select():
    #         print(category.category_name)



    #STORES
            # query = Product.select(Store, Product).where(Product.product_name == product).order_by(Product.product_name).prefetch(Store)

        # for product in query:
        #     print(product.product_name)
        #     for store in Store:
        #         print('  *', store.store_name)

        # for store in Product.select(Store, Product).where(Product.product_name == product):
        #     print(store)

        # for store in Store.select().join(ProductStore).where(Product.product_name == product): #, product_id)))
        #     print(store, product.product_name)
        
        # for store, product in ProductStore.select().where(Store.store_name == ProductStore.store):
        #     print(store, product)


        # query = Product.select().where(Product.product_name == product).order_by(Product.product_name).prefetch(Store)

        # for product in query:
        #     print(product.product_name)
        #     for store in Store:
        #         print('  *', store.store_name)


        # for product in Product.select(Product.product_name == product)\
        # .join(Store) \
        # .where(Product.product_name, Store.store_name):
        #     print(product.product_name,"in", Store.store_name)
