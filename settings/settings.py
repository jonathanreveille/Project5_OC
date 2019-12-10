""" This module is created to stock all
constants for this application """

# URL of OpenFoodFact for API
URL = "https://fr.openfoodfacts.org/cgi/search.pl"


# Database connexion for application - MySQL
NAME_DB = 'p5_db'
USER = 'student'
PASSWORD = 'student'
HOST = '127.0.0.1'
PORT = 3306
CHARSET = 'utf8mb4'


# To download different data from different - Categories
CATEGORY = ["pizza", "frommage", "jus de fruit", "confiture","riz"]

#keywords
KEYWORDS = ["product_name_fr", "main_category_fr", "nutrition_grade_fr", "id", "brands", "stores"]

#Parameter of page size for collecting data from the API 
SIZE = 10
