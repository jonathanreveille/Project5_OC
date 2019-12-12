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



