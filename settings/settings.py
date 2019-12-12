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

CATEGORIES = ["pizza", "riz"]

# Keywords
KEYWORDS = ["product_name_fr", "main_category_fr",
            "nutrition_grade_fr", "id", "br  ands", "stores"]