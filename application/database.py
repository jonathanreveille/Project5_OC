#! /usr/bin/env python3
# coding : utf-8

from peewee import MySQLDatabase
from settings.constants import NAME_DB, USER, PASSWORD, HOST, PORT, CHARSET

db = MySQLDatabase(NAME_DB, user=USER, password=PASSWORD,
host=HOST, port=PORT, charset=CHARSET)


def main():
    pass

if __name__ == "__main__":
    pass



