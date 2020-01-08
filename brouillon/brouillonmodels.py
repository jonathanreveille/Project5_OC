# #! /usr/bin/env python3
# # coding : utf-8

# class Store: 
#     """ This class contains all information 
#     about stores """

#     def __init__(self, store):
#         self.name = store

#     def __repr__(self):
#         f"Store (name: {self.name})"


# class Category:
#     """ This class contains all the information 
#     about Categories """

#     def __init__(self, category):
#         self.name = category

#     def __repr__(self):
#         f"Category (name: {self.name})"


# class Brand:
#     """ This class contains all the information 
#     about the Brands"""

#     def __init__(self, brand):
#         self.name = brand

#     def __repr__(self):
#         f"Brand(name: {self.name})"


# class Product:
#     """ This class contains all information about product """

#     def __init__(self, code, url, product_name, stores, brands, nutrition_grade_fr, ingredients, categories, **kwargs):
        
#         self.code = code
#         self.name = product_name
#         self.url = url
#         self.brands = brands
#         self.nutrition_grade = nutrition_grade_fr
#         self.category = categories
#         self.stores = []

        # for store in stores.split(","):
        #     self.stores.append(Store(store.lower().strip()))
        

#     def __repr__(self):
#         return f"Product(name: {self.name})"





# def main():
#     pass

# if __name__ == "__main__":
#     pass




#     # @classmethod
#     # def is_valid(cls, product):
#     #     """ This method is to check if our product is valid
#     #     according to the parameters we want """

#     #     parameters = ("nutrition_grade_fr","product_name",\
#     #         "code", "brands","stores","url")

#     #     for parameter in parameters:

#     #         if parameter not in product or not product[parameter]:
#     #             return False
#     #     return True


#     # for parameter in parameters:
#     #     if parameter not in product or not product[parameter]:
#     #         not_valid_products.append(product)
#     #         print("-->DEBUGGING", product.get('product_name'), f"{parameter} not present or empty")
#     #         return False
#     #     else:
#     #         return True



#     # def is_valid(self, product):
#     #     """ This method is to check if all the data that 
#     #     we need are present and also, not empty """
#     #     # vérifier que les données sont là,
#     #     # vérifier si elles contiennent une donnée

#     #     is_valid = True

#     #     fields = ("product_name", "nutrition_grade_fr", "code", "brands", "stores", "url", "categories")

#     #     for field in fields:

#     #         if field not in product: #before : self.data_product
#     #             print("DEBBUGING --> there is a missing field or not info on product:", k, f"{field} in", self.data_product.get("product_name"))
#     #             return is_valid == False

#     #         elif not product:
#     #             return is_valid == False

#     #         return True
    

#         # self.final_list = [] # empty list to store all final products

#         # for product in self.data_product["products"]:

#         #     if not is_valid(*product):
#         #         continue
#         #         print("DEBUG", self.data_product.get('product_name'), "is present and has all info")

#         #     if is_valid(*product) == True:
            
#         #         self.cleaned_product.append(Product(**product))

#         # return self.cleaned_product


# dictionnaire = {'data_quality_errors_tags': [], 'additives_old_n': 4, 'emb_codes_orig': '', 'countries_tags': ['en:belgium', 'en:canada', 'en:france', 'en:guadeloupe', 'en:new-caledonia', 'en:reunion', 'en:switzerland'], 'image_ingredients_small_url': 'https://static.openfoodfacts.org/images/products/762/221/044/9283/ingredients_fr.288.200.jpg', 'ingredients_text_debug_tags': [], 'states': 'en:checked, en:complete, en:nutrition-facts-completed, en:ingredients-completed, en:expiration-date-completed, en:packaging-code-to-be-completed, en:characteristics-completed, en:categories-completed, en:brands-completed, en:packaging-completed, en:quantity-completed, en:product-name-completed, en:photos-validated, en:photos-uploaded', 'nucleotides_prev_tags': [], 'nutrition_score_beverage': 0, 'image_url': 'https://static.openfoodfacts.org/images/products/762/221/044/9283/front_fr.286.400.jpg', 'data_sources_tags': ['app-yuka', 'apps'], 'environment_impact_level_tags': [], 'allergens_from_ingredients': 'blé, lécithine de soja, lactose, protéines de lait'}

# print(dictionnaire["allergens_from_ingredients"])

# for d in dictionnaire:
#     for key in d:
#         print(d[key])

#    # print(key[value])

# "data_quality_errors_tags" in dictionnaire


# def find_in_dict(field=str()):
#     """ FONCTION POUR AJOUTER A MA LISTE LA VALEUR 
#     DE LA CLE DU DICTIONNAIRE """

#     if field in dictionnaire[field] or dictionnaire: # SI LE CHAMPS EST PRESENT
#         print(field[key])

# find_in_dict("allergens_from_ingredients")
