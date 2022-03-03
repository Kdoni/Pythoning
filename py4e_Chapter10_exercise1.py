"""
Exercise 1: Revise a previous program as follows: Read and parse the
“From” lines and pull out the addresses from the line. Count the number of messages from each person using a dictionary.
After all the data has been read, print the person with the most commits
by creating a list of (count, email) tuples from the dictionary. Then
sort the list in reverse order and print out the person who has the most
commits.

Sample Line:
From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
Enter a file name: mbox-short.txt
cwen@iupui.edu 5
Enter a file name: mbox.txt
zqian@umich.edu 195
"""

while True:
    fhand=input("Please enter a file name:")
    try:
        x=open(fhand, "r")
        break
    except:
        print("The file name you have entered is not valid...")
        continue
d={}
l=[]

for line in x:
    if not line.startswith("From "):
        continue
    line=line.split()
    word=line[1]
    d[word]=d.get(word,0)+1
for count,email in d.items():
    l.append((email,count))
l.sort(reverse=True)
y=max(l)
print(y[1],y[0])

#       or
# # w= [(y[1], y[0]) for y in l]
# print(w[0])

#line17-24: A standard set up of an input request from the user.
#line25-26: Setting up and empty dictionary and list respectively for use.
#line28-30: Starts a for loop searching the lines in x, ignoring those that do not start with "From ".
#line31-32: We split the line in to a list of its components separated by space, whitespace, and assign to a new variable the 2nd word of the list.
#line33: We add to the empty dictionary a key of the above variable, adding to that the default number 0 added by 1 each time the variable is met.
#line34-35: a for loop with the tuple of the of the dictionary in both key and value, in that order, make a list with that tuple, but in reverse order.
#line36: Sort the list(comaring the count(numbers)) in declining order.
#line37: Set a new variable to the largest number.
#line38-: Showcase the result in reverse order, first the email followed by the count.