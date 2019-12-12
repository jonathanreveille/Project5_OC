#! /usr/bin/env python3
# coding : utf-8

from .database import db
from peewee import Model, BigIntegerField, AutoField, IntegerField, CharField, TextField, ForeignKeyField, CompositeKey, create_tables

# Class base that takes a Model in argument
# model definitions -- the standard "pattern" is to define a base model class
# that specifies which database to use.  then, any subclasses will automatically
# use the correct storage


class Base(Model):
    class Meta:
        database = db


class Category(Base):
    category_name = CharField(unique=True)


class Store(Base):
    store_name = CharField(unique=True)


class Brand(Base):
    brand_name = CharField(unique=True)

# my models : the product model specifies its fields (or columns) declaratively


class Product(Base):
    code = BigIntegerField(unique=True)
    product_name = CharField(max_length=55, null=False)
    description = TextField()
    url_name = CharField(max_length=255, null=False)
    category = ForeignKeyField(Category, backref="category")
    nutriscore = CharField(max_length=1, null=False)
    has_palm_oil = CharField(max_length=3, null=False)
    brand = ForeignKeyField(Brand, backref="product")


class ProductStore(Base):
    product = ForeignKeyField(Product, backref="product_id")
    store = ForeignKeyField(Store, backref="store_id")

    class Meta:
        indexes = (('product', 'store'), True)
        primary_key = CompositeKey('product', 'store')


class Favorite(Base):
    product = ForeignKeyField(Product, backref="product")
    to_replace_with = ForeignKeyField(Product, backref="new_product")

    class Meta:
        indexes = (('from_product', 'to_replace_with'), True)


def main():
    db.create_tables([
        Category, Store, Product, ProductStore, Brand, Favorite
    ])


if __name__ == "__main__":
    main()


# IT WORKS !!!!!!
