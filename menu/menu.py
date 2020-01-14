#! /usr/bin/env python3
# coding : utf-8


class Menu:
    """ this class is to create a list of menu for the 
    client interface"""

    
    def __init__(self, entries):
        self.entries = entries

    def __str__(self):
        """ This method is to create the options of the menu
        and it allows to show in string the menu the way 
        we want """
        #   index  + 1 and  then  name  of  category for example
        #  for index  and  category in  menu entries
        #  return  with  "\n" and  join
        lines = [f"{i+1} : {cat}" for i, cat in enumerate(self.entries)] # index +1 : category

        return "\n".join(lines)


    def __getitem__(self, choice):
        """ this method  is  to  select  an option from the 
        menu, it will check  if the menu option exists """

        if not (0 < int(choice) <= len(self.entries)): #if choice is not in the range of self.entries possible

            raise  ValueError("choice is not valid")  #raise an error here

        return  self.entries[int(choice) -1]  #or select the entry from the user and minus 1 (since  1st position is 0 in our list of entries)

        
    def is_valid_choice(self, choice):
        """  this method is  to  verify if the  choosen 
        option is available in the menu """

        if not choice.isdigit(): #if choice is not  a number
            return False

        if 0 < int(choice) <= len(self.entries): #if choice is in between 0 and the length of  self.entries
            return  True
        return False #else : it's false


