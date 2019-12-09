# OpenClassRooms project: 5
*This is the fifth project in part of the Python course at OC*
*Application that helps you choosing better food*

## :snake: Python App Development - Project 5 - Purbeurre !

Here is the [link](https://github.com/jonathanreveille/OC_projet5.git) to the project

### The project
For this project, we had to create an application that allows the user seek for food alternatives. 
Why food alternatives?
Because it seems that product nutrition tables aren't easy to 
de-code in-store, this is why we generated this application in order 
to ease your daily life when you are seeking for healthier food 
at your own neighborehood store.

So far this application workds under the **terminal mode**. We will 
provide graphics into the next versions of this application.

### Description of the project (application) :
The program will ask the user to choose between two options : 
1- Which food product do you wish to replace ? (SEEK FOR PRODUCT)
// 2- See your favorites for alternative products (FAVORITES)

If the user selects 1:
- the program will now ask the user to select a category (input : a number) and then press 'enter'
- the program will now ask the user to select a product OR he can do a 'search'
- the program will show some information from a selected product, and he will then suggest alternatives (with better nutriscore for the user's health)

### What is in this project ?
- Use of OOP
- Use of pipenv (virtual environment with Python 3)
- Respect and follow recommandations from PEP8

### Getting started:

First of all, first you need to **install pipenv**

* `pipenv install` (install all requirements)
This will install all *requirements* that is required for 
this project (peewee, pymsql, requests and python 3.7)

The advantage of pipenv is that it is cross-platform. It is 
recommended by the official documentation.


### Launch the app
 
* `pipenv run python -m main`

### Licence:
* Use of OpenFoodFacts datas[link](https://fr.openfoodfacts.org)

### Acknowledgement:
I would like to give special thanks to ***Thierry Chappuis***
for guiding me throughout this project.