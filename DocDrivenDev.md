
# Doc Driven Development

## :snake: Python App Development - Project 5 - Purbeurre - OC !

## Package bdd : 

*dbconnexion.py*

- code to connect to database


*models.py*

- Create all tables with PEEWEE syntax (Brand, Store, Category, Product, ProductStore, Favorite)

- Function to create_tables (safe=True).
Save = True is the equivalent : DROP IF EXISTS in SQL language.


*productmanager.py*

- function get_all_products_from_db(self): this method is to access all product name from database.

- function get_all_category(self): this method is to get all categories from the database.

- function get_products_from_category(self, category) : This method is to get all products from a category.

- function get_unhealthy_products(self, category): this method is to get all unhealthy product from a category
from the database.

- function get_healthy_products(self, category): this method is to get all healthy product from a category from the database.

- function get_data_from_substitute(self, product):
this method is to get all the additionnal information about a
product that the user selects to save to his favorites."""

- function get_url_from_product(self, product_name):
This method is to get specific url from product in the database"""

favoritemanager.py :

- function save_to_favorites(self, original, substitute): this method will join a product to replace by an healthier choice.

- function show_favorites(self): this method shows the foreign keys of products that has been saved into the user's favorite table."""


## Package menu :

*menu.py*

- class Menu and MenuHome

- __getitem__(self, choice):this method  is  to  select  an option from the menu, it will check  if the menu option exists.

- function is_valid_choice(self, choice): this method is  to  verify if the  choosen
option is available in the menu """


*client.py*

- menu0(self): This menu will ask user what he wishes to do on the application.

- menu1(self): CATEGORY MENU
this method shows all the present categories to the user in this menu.

- menu2(self): UNHEALTHY PRODUCT MENU
This method shows the menu of products for the user. 

- menu3(self): This method is to show the menu of substitutes products for the user.

- menu4(self): This method shows the store where we can buy the product.

- menu5(self): this method is the menu where all favorite products were saved by
the user.

- menu6(self): This menu shows all the products that have been saved by the user

- back_home(self):
this method is to get back at the main menu deleting all other past
search from user's session.

- quit_app(self):
This method manages the option quit 1 from the menu for the client's
interface.



## Package models


*downloader.py*

- function check_connexion(self):
This method is to download all data needed
from the URL,
output = if <Response 200> params : OK
and url == everything is well set.

- function fetch_data_from_API(self):
This method is to transform what we received from the API into .json format.
We get in return a dictionnary field with data.

- function is_valid_data(self, product):
This method to validate the data that is present and complete.
        --> we create a list of fields we want to search;
        --> check if the key exists;
        --> check if value exists for the key.

- function get_product_data(self):
This method is to add to at our product (list) only the values from
the keys that we need."""


- function fill_product(self): This method is to create all objects in database.


- function create_object_by_category(self): This module is to create all the different categories
that we will need for our application.


