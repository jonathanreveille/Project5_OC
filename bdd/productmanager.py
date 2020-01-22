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
                    (Category.category_name == self.query) \
                    & (Product.nutrition_grade_fr >= "c")\
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

            
    # def get_healthy_products2(self, category):
    #     """ this method is to get all healthy product from a category
    #     from the database """

    #     self.query = category 

    #     for product in (Product
    #             .select(Product.product_name, Product.category, Product.nutrition_grade_fr)
    #             .join(Category)
    #             .where(
    #                 (Category.category_name == self.query) \
    #                 & (Product.nutrition_grade_fr <= "b")
    #             )
    #             .order_by(fn.Rand()).limit(10)
    #         ):

    #         print(product.product_name, " >> ", product.nutrition_grade_fr.upper(), "(nutriscore)")


    # def get_store_name_for_product2(self, product): # THIS WORKS WELL
    #     """ get name of stores where we can buy a product """

    #     self.query = product

    #     for store in (Store.select()
    #     .join(ProductStore)
    #     .join(Product)
    #     .where(Product.product_name == self.query)):
            
    #         print(self.query, "in stores >> ", store.store_name.capitalize())
                    

        #return list(Store.select().join(ProductStore).join(Product).where(Product.product_name == self.query))

            # print(store.store_name)

            # print(
            #     product.product_name,
            #     ">> nutriscore: ", product.nutrition_grade_fr.upper(),
            #     " - more info >>",product.url
            #     )






#productmanager = ProductManager()
#productmanager.get_unhealthy_products("Pizza")  #WORKS MARVELOUSLY
#productmanager.get_healthy_products2("chips") #WORKS MARVELOUSLY
#productmanager.get_store_name_for_product2("Fraîch'Up Little Italy Italian Burger") #WORKS MARVELOUSLY
# productmanager.get_data_from_substitute("Fraîch'Up Little Italy Italian Burger") #WORKS MARVELOUSLY



#productmanager.get_all_category() # works
#productmanager.get_products_from_category("Biscuits") #works
#productmanager.get_healthy_products_from_category("Pizza") # works
#productmanager.get_all_products_from_db() #works
#productmanager.get_all_category() #works
#productmanager.get_unhealthy_product_from_category("Pizza")
#productmanager.get_store_name_from_product("Pizza Kebab") # works >>> Auchan
#productmanager.get_healthy_product_from_category("Pizza") #works but show all the product
#productmanager.get_store_name() # still need to work on it
#productmanager.get_all_products_from_db() #works
#productmanager.get_products_from_category("Biscuits") #works
#productmanager.show_products_from_category("Pizza") #works
#productmanager.get_store_name() # works


        # for product in (Product
        #         .select(Product.product_name, Product.category, Product.nutrition_grade_fr)
        #         .join(Category)
        #         .where(
        #             (Category.category_name == self.query) \
        #             & (Product.nutrition_grade_fr >= "c")\
        #         )
        #         .order_by(fn.Rand()).limit(10)
        #     ):

        #     print(product.product_name, " >> ", product.nutrition_grade_fr.upper(), "(nutriscore)")



    # def get_unhealthy_product_from_category(self, category):
    #     """ This method gets all products from one category
    #     ordered by its nutriscore (from worst to best)"""

    #     self.query = category

    #     for product in Product.select() \
    #     .join(Category) \
    #     .where(
    #         (Category.category_name == self.query) \
    #         | (fn.Lower(fn.Substr(Product.nutrition_grade_fr,1, 1)) == "c") \
    #         | (fn.Lower(fn.Substr(Product.nutrition_grade_fr,1, 1)) == "d") \
    #         | (fn.Lower(fn.Substr(Product.nutrition_grade_fr,1, 1)) == "e") \
    #         .order_by(fn.Rand()).limit(10)
    #         ): # IT WORKS 

    #         print(product.product_name,"-->", product.nutrition_grade_fr.upper(), "(nutriscore)")



    # def get_unhealthy_product_from_category2(self, category):
    #     """ This method gets all products from one category
    #     ordered by its nutriscore (from worst to best)"""

    #     for product in Product.select() \
    #     .join(Category, JOIN.LEFT_OUTER, on=(Product.category == Category.category_name)) \
    #     .where(
    #         (Category.category_name == category) \
    #         |(Product.nutrition_grade_fr == "c") \
    #         |(Product.nutrition_grade_fr == "d") \
    #         |(Product.nutrition_grade_fr == "e"))\
    #         .order_by(fn.Rand()).limit(10):

    #         print(product.product_name,"-->", product.nutrition_grade_fr, "(nutriscore)")
           
    
    # def get_unhealthy_product_from_category3(self, category):
    #     """ This method gets all products from one category
    #     ordered by its nutriscore (from worst to best)"""

    #     self.query = category

    #     for product in Product.select() \
    #     .join(Category) \
    #     .where(Category.category_name == category) \
    #     .order_by(Product.nutrition_grade_fr.desc()).limit(10):

    #         print(product.product_name,"-->", product.nutrition_grade_fr, "(nutriscore)")


    # def get_unhealthy_product_from_category4(self, category):
    #     """ This method gets all products from one category
    #     ordered by its nutriscore (from worst to best)"""

    #     self.query = category

    #     for product in Product.select() \
    #     .join(Category) \
    #     .where(Category.category_name == self.query) \
    #     .order_by(Product.nutrition_grade_fr.desc()).limit(10):

    #         print(product.product_name,"-->", product.nutrition_grade_fr, "(nutriscore)")

        # WORKS TOG ET ALL PRODUCTS FROM 1 category



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


    # def get_unhealthy_products_from_category2(self, category):
    #     """ This method  shows  all healthy product from the selected
    #     category (from best to worst) """

    #     self.query = category

    #     for product in Product.select().join(Category) \
    #     .where(Category.category_name == self.query) \
    #     .order_by(fn.Rand()).limit(10):

    #         print(product.product_name, "nutriscore est:  ", product.nutrition_grade_fr.upper())


    # def get_unhealthy_product_from_category1(self, category):
    #     """ This method gets all products from one category
    #     ordered by its nutriscore (from worst to best)"""

    #     self.query = category 

    #     for product in Product.select() \
    #     .join(Category) \
    #     .where(
    #         (Category.category_name == self.query)\
    #         |(Product.nutrition_grade_fr == "c") \
    #         |(Product.nutrition_grade_fr == "d") \
    #         |(Product.nutrition_grade_fr == "e")) \
    #         .order_by(fn.Rand()).limit(10):

    #         print(product.product_name,"-->", product.nutrition_grade_fr, "(nutriscore)")
 