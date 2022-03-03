"""
Exercise 3: Write a program that reads a file and prints the letters
in decreasing order of frequency. Your program should convert all the
input to lower case and only count the letters a-z. Your program should
not count spaces, digits, punctuation, or anything other than the letters
a-z. Find text samples from several different languages and see how
letter frequency varies between languages. Compare your results with
the tables at https://wikipedia.org/wiki/Letter_frequencies.
"""

#Prompting the user to enter their input:
while True:
    fhand=input("Please insert a file name:")
    try:
        x=open(fhand, "r")
        break
    except:
        print("The file name you have entered is not valid...\nplease try again...\n")
        continue

import string
y=list(string.ascii_lowercase)
d={}
l=[]
g=""
totalCount=0
contents = x.read()
for abc in contents:
    if abc in y:
        d[abc]=d.get(abc,0)+1
        totalCount+=1


# for line in x:
#     line = line.translate(str.maketrans('', '', string.punctuation))
#     line=line.lower()
#     words=line.split()
#     for word in words:
#         letter=list(word)
#         for abc in letter:
#             d[abc]=d.get(abc,0)+1


for az,counter in d.items():
    l.append((counter,az))
    l.sort(reverse=True)
for item in l:
    # if item[1] in y:  Not necessary in this stage since, we have filtered the text's letters in line 29.
        g=g+item[1]
        print(item[1],round((item[0]/totalCount)*100,2),"%")
        
print("The word frequency of the text",fhand,"is the following:\n"+g)

#Analysis:
'''Line21-22: Importing a library and making a list with all the 26 letters of the english alphabet
    Line 23-26: Setting up all the variables, outside their respective loops, for later use
    line27:Reads through the whole text as a single string.
    line28-31: For every character in the text, if that character exists in the list with all the letters,
    add that to the dictionary along with its count of repetitions as its value, and increase the value of totalCount
    by 1, each time a letter is added to the dictionary
    line34-42: At first I pressumed that in order to read through each character of a text, I had to break the text into
    lines, the lines into words and the words into letters. However, reading through the whole text as a single string
    makes the program 6 lines of code shorter.
    Line44-46: For the keys and values respectively in the dictionary, add them in reverse order into a new list and sort it out in descending order.
    Line49: For every item(tuple) in the list, make a variable with only the values(meaning the letters in this case)
    Line50: Print the the 2nd elements of the tupples and the frequency percentage, rounded up in two decimals.
    Line52: According to wikipedia, another way of showcasing word frequency is to present a single string with all the 
    letters in descending order, one next to another.
    '''