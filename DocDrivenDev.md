
# Doc Driven Development

## :snake: Python App Development - Project 5 - Purbeurre - OC

## Package bdd : 

*dbconnexion.py*

- Code to connect to database


*models.py*

- Create all tables with PEEWEE syntax (Brand, Store, Category, Product, ProductStore, Favorite)

- Function to create_tables (safe=True).
Save = True; is the equivalent of : DROP IF EXISTS in SQL language.


*productmanager.py*

- Class ProductManager

- Function get_all_products_from_db(self): this method is to access all product name from database.

- Function get_all_category(self): this method is to get all categories from the database.

- Function get_products_from_category(self, category) : This method is to get all products from a category.

- Function get_unhealthy_products(self, category): this method is to get all unhealthy product from a category
from the database.

- Function get_healthy_products(self, category): this method is to get all healthy product from a category from the database.

- Function get_data_from_substitute(self, product): this method is to get all the additionnal information about a
product that the user selects to save to his favorites.

- Function get_url_from_product(self, product_name): This method is to get specific url from product in the database.


*favoritemanager.py*

- Class FavoriteManager

- Function save_to_favorites(self, original, substitute): this method will make us save a product into our favorites.

- Function show_favorites(self): this method shows the product_name from the foreign keys 
product that is saved into the Favorite table.


## Package menu :

*menu.py*

- Class Menu and MenuHome

- __getitem__(self, choice): this method  is  to  select  an option from the menu, it will check  if the menu option exists.

- Function is_valid_choice(self, choice): this method is  to  verify if the  choosen
option is available in the menu.


*client.py*

- Class Client

- Function menu0(self): this menu will ask user what he wishes to do on the application.

- Function menu1(self): CATEGORY MENU,
This method shows all the present categories to the user in this menu.

- Function menu2(self): UNHEALTHY PRODUCT MENU,
This method shows the menu of products for the user. 

- Function menu3(self): HEALTHY PRODUCT MENU,
This method is to show the menu of substitutes products for the user.


- Function menu4(self): This method ask if the user wants to add to favorite the product he selected from the healthy list of products.

- Function menu5(self): This method warns the user that his search has been
saved to his favorites, and it asks him if he wants to go his favorite menu.

- Function menu6(self): This menu shows all the products that have been saved to Favorites by the user.

- Function back_home(self): This method is to get back at the main menu deleting all other past
search from user's session.

- Function quit_app(self): This method manages the option quit 1 from the menu for the client's interface.



## Package models

*downloader.py*

- Class Downloader

- Function check_connexion(self):
This method is to download all data needed
from the URL,
output = if <Response 200> params : OK
and url == everything is well set.

- Function fetch_data_from_API(self):
This method is to transform what we received from the API into .json format.
We get in return a dictionnary field with data.

- Function is_valid_data(self, product):
This method to validate the data that is present and complete.
        --> we create a list of fields we want to search;
        --> check if the key exists;
        --> check if value exists for the key.

- Function get_product_data(self):
This method is to add to at our product (list) only the values from
the keys that we need.

- Function fill_product(self): This method is to create all objects in database.

- Function create_object_by_category(self): This module is to create all the different categories
that we will need for our application.
