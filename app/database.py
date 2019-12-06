#! /usr/bin/env python3
# coding : utf-8
from peewee import MySQLDatabase


# Connect to a MySQL database on network.
db = MySQLDatabase('p5_db', user='student', password='student',
                         host='127.0.0.1', port=3306, charset='utf8mb4')
