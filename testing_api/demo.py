#! /usr/bin/env python3
# coding : utf-8

import requests

#Si on veut trouver les 50 produits les plus populaires de Lindt

payload = {"search_terms": "Herta",
            "search_tag": "brands", 
            "sort_by": "unique_scans_n", # popularité
            "page_size": 10,
            "json": 1}
res = requests.get("https://fr.openfoodfacts.org/cgi/search.pl?", params=payload)


# l'url correspondante
#res.url
#'https://fr.openfoodfacts.org/cgi/search.pl?search_terms=Lindt&search_tag=brands&sort_by=unique_scans_n&page_size=10&json=1'

# on peut ensuite récupérer les produits
results = res.json()
results.keys()
products = results["products"]

print("voir le nombre d'attribut du produit")
len(products)

# Et afficher leurs noms
for product in products:
    print(product["product_name"])


for product in products:
    print(product["origins"])

for product in products:
    print(product["nutrition_grades"])
