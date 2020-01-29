#! /usr/bin/env python3
# coding : utf-8

from .models import Favorite, Product


class FavoriteManager():
    """this class handles the favorites of the user."""

    def __init__(self):
        self.original = list()
        self.substitute = list()
        self.favorites = list()

    def __str__(self):
        """returns a string of our object."""

        return f"{self.original} is replaced by: {self.substitute}"

    def save_to_favorites(self, original, substitute):
        """this method will join a product to replace by an healthier
        choice."""

        self.original = original
        self.substitute = substitute

        self.favorites.append((self.original, self.substitute))

        for original, substitutes in self.favorites:
            product_obj = Product.get(Product.product_name == self.original)

            for substitute in substitutes:
                sub_obj = Product.get(Product.product_name == self.substitute)
                Favorite.get_or_create(
                                        substituted_product=product_obj,
                                        substitute_products=sub_obj)

    def show_favorites(self):
        """this method shows the foreign keys of products that has been saved
        into the user's favorite table."""

        return list(Favorite.select())
