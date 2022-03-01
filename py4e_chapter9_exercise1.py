"""
Write a program that reads the words in words.txt and stores them as
keys in a dictionary. It doesn’t matter what the values are. Then you
can use the in operator as a fast way to check whether a string is in the
dictionary
"""

dictionary={}
count=0
fhand=open("words.txt","r")
for line in fhand:
    line=line.split()
    for word in line:
        dictionary[word]=count
        count=count+1

        
print('programs' in dictionary)

"""That was not so hard. I started by setting an empty dictionary at the start and a counter, meant to be used as the incremental value of the keys(probably not necessary
Then we split the lines into lists of words separated by spaces. For each of these words add that word to the dictionary with a key, increments of count and increase the value of count by 1
"""