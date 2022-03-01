# testing={}
# testing["lion"]=1
# print(testing)

"""Adding an item in a list
"""

# testing={}
# testing["lion"]=1
# print(testing["lion"])

"""Printing the list's value using the key
"""
# testing={}
# testing["lion"]=1
# print(testing.values())

"""Printing the values of a dictionary
"""

"""
You could create a list with 26 elements. Then you could convert each
character to a number (using the built-in function ord), use the number as
an index into the list, and increment the appropriate counter.
"""

# lista=[0]*26
# import string
# x=list(string.ascii_lowercase)
# for letter in x:
#     y=ord(letter)-97
#     lista[y]+=1
# print(lista)


"""You could create a dictionary with characters as keys and counters as the
corresponding values. The first time you see a character, you would add
an item to the dictionary. After that you would increment the value of an
existing item.
"""


dictionary={}
import string
x=list(string.ascii_lowercase)
x.append("b")
for letter in x:
        dictionary[letter]=dictionary.get(letter,0)+1
print(dictionary)

"""We start by creating an empty dictionary
Then we create a list with all the letter of the english alphabet
we add a duplicate letter on the list, in order to cross examine the results.
Last we initiate a for loop, for every letter in the list,
the dictionary "dictrionary" with key "letter" is the dictionary in which we add the 
key-value pair (parenthesis) setting up the value +1"""


    



