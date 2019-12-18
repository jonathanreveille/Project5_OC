


# def cleanNullTerms(d):

#    clean = {}

#    for k, v in d.items():

#       if isinstance(v, dict):
#         nested = cleanNullTerms(v)

#         if len(nested.keys()) > 0:
#             clean[k] = nested

#         elif v is not None:
#             clean[k] = v

#         return clean
 # print(cleanNullTerms(data))

listing = ['d', 'Prince: Goût Chocolat au Blé Complet', '7622210449283', 'LU,Mondelez', 'Carrefour Market,Magasins U,Auchan,Intermarché,Carrefour,Casino,Leclerc,Cora,Bi1', 'https://fr.openfoodfacts.org/produit/7622210449283/prince-gout-chocolat-au-ble-complet-lu', 'Snacks,Snacks sucrés,Biscuits et gâteaux,Biscuits,Biscuits au chocolat', 'e', 'Nutella biscuits', '8000500310427', 'Nutella,Ferrero,Nutella Biscuits', 'Super U,Intermarchė', 'https://fr.openfoodfacts.org/produit/8000500310427/nutella-biscuits', 'Snacks,Snacks sucrés,Biscuits et gâteaux,Biscuits', 'c', 'Biscuit Sésame', '3175680011480', 'Gerblé', 'carrefour auchan', 'https://fr.openfoodfacts.org/produit/3175680011480/biscuit-sesame-gerble', 'Snacks,Sweet snacks,Biscuits and cakes,Biscuits', 'a', 'Biscuit Pomme Noisette', '3175681851849', 'Gerblé', 'Franprix,Magasins U,Leclerc,E Leclerc,Delhaize', 'https://fr.openfoodfacts.org/produit/3175681851849/biscuit-pomme-noisette-gerble', 'Snacks,Snacks sucrés,Biscuits et gâteaux,Biscuits']

test_dict = {"un":"one", "deux":"two", "trois":"three", "quatre":"four", "cinq":"None"}
print(str(test_dict))

res = {key: test_dict[key] for key in test_dict.keys()
                               & {'deux', 'trois'}} 

res = dict((k, test_dict[k]) for k in ['deux', 'quatre'] 
         if k in test_dict)

print("filtered results are : ", str(res))

# for key in test_dict.items():
#       print(str(test_dict))

   #print(value)

   #if value == None:
      #print(key)

        
        # fields = ["nutrition_grade_fr", "product_name", "code", "brands", "stores", "url", "categories"]

        # zipObject = zip(fields, self.data_product)
        
        # dictOfWords = dict(zipObject)

        #print(str(dictOfWords))

        # for key , value in dictOfWords.items():
        #     print(key, " :: ", value)
        #print(self.data_product)
   

# """
# {
#   'first_name': 'Jonathan',
#   'last_name': 'Hsu',
#   'family': {
#     'mother': 'Mary',
#     'father': 'Peter',
#     'brother': 'Charles'
#   }
# }
# """