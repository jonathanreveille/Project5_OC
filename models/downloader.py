
import requests

from settings.config import CATEGORY_LIST
from bdd.models import Category, Product, Store, Brand, ProductStore


class ProductDownloader:

    """This class has the responsibility to download data from OpenFoodFact
    API."""

    def __init__(self, category):

        self.url = "https://fr.openfoodfacts.org/cgi/search.pl"

        self.params = {
            "action": "process",
            "tagtype_0": "categories",
            "tag_contains_0": "contains",
            "tag_0": category,
            "sort_by": "unique_scans_n",
            "page_size": 250,
            "json": 1
        }

        self.category = category

    def check_connexion(self):
        """ This method is to download all data needed
        from the URL,
        output = if <Response 200> params
        and url == everything is well set"""

        connexion = True
        # self.response = statut.code()
        self.response = requests.get(self.url, params=self.params)
        # si pas de réseau = on arrive sur une exception.

        if not connexion:
            print("<<Not connected to API>>")
        else:
            print("<<Connected to API, loading...>>")

    def fetch_data_from_API(self):
        """This method is to transform what we received from the API into .json
        format.

        We get in return a dictionnary field with data
        """

        self.data_product = self.response.json()
        # type(self.data_product)) -> this a dict
        return self.data_product
        # becomes a list if we add ["products"]
        # to self.data_product.

    def is_valid_data(self, product):
        """This method to validate the data that is present and complete.

        --> we create a list of fields we want to search;
        --> check if the key exists;
        --> check if value exists for the key
        """

        fields = ["product_name", "nutrition_grade_fr",
                  "brands", "stores", "url", "categories", "code"]

        for field in fields:
            if field not in product or not product[field]:
                return False
        return True

    def get_product_data(self):
        """This method is to add to at our product [list] only the values from
        the keys that we need."""

        self.product_list = []

        for product in self.data_product["products"]:

            if self.is_valid_data(product):
                # contains only element with searched fields
                self.product_list.append(product)

        return self.product_list  # return a dict

    def fill_product(self):
        """this method is filter all our stores."""

        category, created = Category.get_or_create(category_name=self.category)

        for product in self.product_list:
            brand, created = Brand.get_or_create(brand_name=product["brands"])

            product_obj, created = Product.get_or_create(
                product_name=product["product_name"][:255],
                code=product["code"],
                nutrition_grade_fr=product["nutrition_grade_fr"],
                url=product["url"],
                brand=brand,
                category=category
            )

            for store_name in product["stores"].split(","):
                store, created = Store.get_or_create(
                    store_name=store_name.strip().lower())
                ProductStore.get_or_create(product=product_obj, store=store)

    def create_object_by_category(self):
        """this module is to create all the different categories that we will
        need for our application."""

        self.check_connexion()
        self.fetch_data_from_API()
        self.get_product_data()
        self.fill_product()
        print("Thanks for waiting ! All data are in your db now")


def main():
    """In this main, you manage your categories."""

    for category in CATEGORY_LIST:
        cat = ProductDownloader(category)
        cat.create_object_by_category()


if __name__ == "__main__":
    main()
