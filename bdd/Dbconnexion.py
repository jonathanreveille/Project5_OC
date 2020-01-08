#! /usr/bin/env python3
# coding : utf-8

from peewee import MySQLDatabase

# Database connexion for application - MySQL
NAME_DB = 'p5_db'
USER = 'student'
PASSWORD = 'student'
HOST = '127.0.0.1'
PORT = 3306
CHARSET = 'utf8mb4'

db = MySQLDatabase(NAME_DB, user=USER, password=PASSWORD,
                   host=HOST, port=PORT, charset=CHARSET)


def main():
    pass

if __name__ == "__main__":
    pass
