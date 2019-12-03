#! /usr/bin/env python3
# coding : utf-8

""" This module is to connect to our DB with MySQL"""

import mysql.connector

cnx = mysql.connector.connect(user='student', password='student',
                              host='127.0.0.1',
                              database='p5_db')

cnx.close()
