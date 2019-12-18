#! /usr/bin/env python3
# coding : utf-8

import requests

# Si on veut trouver les 50 produits les plus populaires de Lindt

payload = {
           "search_tag": "nutrition_grades",
           "tag_0" : "céréales pour petit-déjeuners",
           "sort_by": "unique_scans_n",  # popularité
           "page_size": 100,
           "json": 1}

res = requests.get("https://fr.openfoodfacts.org/cgi/search.pl?", params=payload)

# on peut ensuite récupérer les produits
data = res.json()

products = data["products"]

print(type(products))

#for product in products:
   # print(product["nutrition_grade_fr"])

for product in products:
    print(product["product_name"])

if "nutrition_grade_fr" in products:
    print("True")
else:
    print("Not found")



#for product in products: 
 #   print(product["brands"])

#for product in products:
    #print(product["product_name"])

#for product in products:
    #print(product["categories"])

# l'url correspondante
# res.url
# 'https://fr.openfoodfacts.org/cgi/search.pl?search_terms=Lindt&search_tag=brands&sort_by=unique_scans_n&page_size=10&json=1'


##results.keys()



#print("voir le nombre d'attribut du produit")
#len(products)

# Et afficher leurs noms
#for product in products:
    #print(product["product_name"])






            # print("DEBUG", \
            #     product["nutrition_grade_fr"],product["code"],\
            #     product["categories"], product["product_name"],\
            #     product["stores"], product["url"], product["ingredients"])
            #     # ==> return the list of downloaded product



# is_valid = True 
#         for product in self.products_list:
#             for parameter in parameters:
#                 try:
#                     if parameter not in product or not product[parameter]:
#                         return is_valid == False

#                     elif parameter in product or product[parameter]:
#                         self.cleaned_list.append(Product(**product))

#                 except TypeError as e:
#                     print(f"TypeError, missing a parameter for product...{parameter}", e)
#                     break
            
#                 return self.cleaned_list



    #                 #champs qu'on recherche
    #     fields = ("product_name","nutrition_grade_fr","categories",\
    #             "code", "stores", "brands","code", "url")

    #     #Pour chaque champs dans les fields
    #     for field in fields:
    #         #Si le field n'est pas présent dans la liste ou pas de self.products_list[field] présent:
    #         if field not in self.products_list or not self.products_list[field]:
    #             print("-->DEBUG", self.products.get('product_name'), f"{field} not present or empty")
    #             return False
    #         return True