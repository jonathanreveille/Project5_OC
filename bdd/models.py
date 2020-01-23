#! /usr/bin/env python3
# coding : utf-8

from .Dbconnexion import db
from peewee import (Model,
BigIntegerField,
CharField,
TextField,
ForeignKeyField,
CompositeKey,
PrimaryKeyField)

# import logging

# logger = logging.getLogger('peewee') 
# logger.addHandler(logging.StreamHandler()) 
# logger.setLevel(logging.DEBUG)


# Class base that takes a Model in argument
# model definitions -- the standard "pattern" is to define a base model class
# that specifies which database to use.  then, any subclasses will automatically
# use the correct storage


class Base(Model):
    class Meta:
        database = db


class Category(Base): # my models : the product model specifies its fields (or columns) declaratively
    category_name = CharField(unique = True)

    class Meta: #Meta information -->additional information than the columns from the table itself. 
        table_name = "category" # for example here, we add a table_name as an additional data about the table


class Brand(Base):
    brand_name = CharField(unique = True)

    class Meta: #additional information
        table_name = "brand"


class Store(Base): # a modifier comme dans l'exemple de la documentation (relation ManyToMany avec Product et Store)
    store_name = CharField(unique = True)

    class Meta: #additional information
        table_name = "store"


class Product(Base):
    code = BigIntegerField(primary_key= True)
    product_name = CharField(max_length = 255)
    url = CharField(max_length = 255, null = False)
    nutrition_grade_fr = CharField(max_length=1)
    brand = ForeignKeyField(Brand, backref = "products")
    category = ForeignKeyField(Category, backref= "products") #backref va créer un attribut dans mes objets de type catégory. un attribut qui me permet  d'acceder à un 

    class Meta:
        table_name = "product"


class ProductStore(Base):
    product = ForeignKeyField(Product, backref = "product_store_set")
    store = ForeignKeyField(Store, backref = "product_store_set")

    class Meta:
        table_name = "product_store"
        indexes = ((('product', 'store'), True),)


class Favorite(Base):
    substituted_product = ForeignKeyField(Product, backref= "substituted_products_as_favorite")
    substitute_products = ForeignKeyField(Product, backref = "substitute_products_as_favorite")

    class Meta:
        table_name = "favorite"

# simple utility function to create tables

def create_tables():
    with db:
        db.create_tables([Category, Store, Brand, Product, ProductStore, Favorite], safe=True)


create_tables()



# IT WORKS !!!!!!

        
# ProductStore = Product.stores.get_through_model()


# class ProductStore(Base):
#     product = ForeignKeyField(Product, unique=True, null = False)
#     store = ForeignKeyField(Store, unique=True, null= False)

#     class Meta:
#         table_name = "productstore"




# class ProductStore(Base):
#     product = ForeignKeyField(Product, backref="product_id")
#     store = ForeignKeyField(Store, backref="store_id")

#     class Meta: # c'est de la meta information (supplémentaire en plus des infos déjà donnée au dessus
#         table_name = "productstore"
#         indexes = (('product', 'store'), True)
#         primary_key = CompositeKey('product', 'store')


# class Favorite(Base):
#     product = ForeignKeyField(Product, backref="product")
#     to_replace_with = ForeignKeyField(Product, backref="new_product")

#     class Meta:
#         table_name = "favorite"
#         indexes = ((('from_product', 'to_replace_with'), True))

