#! /usr/bin/env python3
# coding : utf-8

import requests

# The main URL where we gather our data from OFF
url = "https://fr.openfoodfacts.org/cgi/search.pl"

# Empty variable to stock products, called products
products = []

# Different categories that we want to extract from OFF API

CATEGORIES = [
    "pâte à tartiner",
    "beurre végétale",
    "frommage à tartiner",
    "..."
]

# Customizing the OFF URL with different parameters
# Those are the parameters to customize for the URL
# Set it as dictionnary to make request work

for category in CATEGORIES: #Parameters
    params = { 
        "action": "process",
        "tagtype_0": "categories",
        "tag_contains_0": "contains",
        "tag_0": category,
        "sort_by": "unique_scans_n",
        "page_size": 500,
        "json": 1,
    }


response = requests.get(url, params=params) #get the data 

# We call the .json method from request to get the json file of the seeked page
data = response.json()

for product in data['products']:
    product['purbeurre-category'] = category
    products.append(product)k