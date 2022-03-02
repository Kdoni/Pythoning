"""
Exercise 3: Write a program to read through a mail log, build a histogram using a dictionary to count how many messages have come from
each email address, and print the dictionary.

Enter file name: mbox-short.txt
{'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3,
'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,
'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3,
'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1,
'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2,
'ray@media.berkeley.edu': 1}
"""

while True:
    fhand=input("Please insert a file name:")
    try:
        x=open(fhand, "r")
        break
    except:
        print("The file name you have entered is not valid...")
        continue
d={}
for line in x:
    if not line.startswith("From "):
        continue
    line=line.split()
    word=line[1]
    d[word]=d.get(word,0)+1
print(d)

#Pretty much identical to exercise 2 of Chapter 9