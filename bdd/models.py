#! /usr/bin/env python3
# coding : utf-8

from .Dbconnexion import db
from peewee import (Model,
                    BigIntegerField,
                    CharField,
                    ForeignKeyField)

# import logging

# logger = logging.getLogger('peewee')
# logger.addHandler(logging.StreamHandler())
# logger.setLevel(logging.DEBUG)


class Base(Model):
    class Meta:
        database = db


class Category(Base):
    category_name = CharField(unique=True)

    # Meta information -->additional information
    class Meta:
        table_name = "category"


class Brand(Base):
    brand_name = CharField(unique=True)

    class Meta:  # additional information
        table_name = "brand"


class Store(Base):
    # relation ManyToMany avec Product et Store
    store_name = CharField(unique=True)

    class Meta:  # additional information
        table_name = "store"


class Product(Base):
    code = BigIntegerField(primary_key=True)
    product_name = CharField(max_length=255)
    url = CharField(max_length=255, null=False)
    nutrition_grade_fr = CharField(max_length=1)
    brand = ForeignKeyField(Brand, backref="products")
    category = ForeignKeyField(Category, backref="products")

    class Meta:
        table_name = "product"


class ProductStore(Base):
    product = ForeignKeyField(Product, backref="product_store_set")
    store = ForeignKeyField(Store, backref="product_store_set")

    class Meta:
        table_name = "product_store"
        indexes = ((('product', 'store'), True),)


class Favorite(Base):
    substituted_product = ForeignKeyField(
        Product, backref="substituted_products_as_favorite")
    substitute_products = ForeignKeyField(
        Product, backref="substitute_products_as_favorite")

    class Meta:
        table_name = "favorite"


def create_tables():
    with db:
        db.create_tables([Category, Store, Brand, Product,
                          ProductStore, Favorite], safe=True)


create_tables()
