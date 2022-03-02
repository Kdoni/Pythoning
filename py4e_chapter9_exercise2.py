"""Exercise 2: Write a program that categorizes each mail message by
which day of the week the commit was done. To do this look for lines
that start with “From”, then look for the third word and keep a running
count of each of the days of the week. At the end of the program print
out the contents of your dictionary (order does not matter).
Sample Line:
From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
Sample Execution:
python dow.py
Enter a file name: mbox-short.txt
{'Fri': 20, 'Thu': 6, 'Sat': 1}
"""

while True:
    fhand=input("Please enter a file name:")
    try:
        x=open(fhand,"r")
        break
    except:
        print("The file name you have entered is not valid...")
        continue
d={}
for line in x:
    if not line.startswith("From "):
        continue
    line=line.split()
    word=line[2]
    d[word]=d.get(word,0)+1
print(d)

#Again an easy one: line14-21: Setting a pretty standard guardian in case of mismatch.
#line22:Setting up an empty dictionary
#23-25: Setting up a for loop to exlude all the lines that do not start with ("From")
#line26:Spliting up each line, that starts with "From" into a list of words.
#line27: From that list a new variable will be the 3rd word of the selected lines.
#line28: We add to the empty dictionary the variable word as its key with value 0+1 for counting the frequency of repeated words.
