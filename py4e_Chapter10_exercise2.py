"""
Exercise 2: This program counts the distribution of the hour of the day
for each of the messages. You can pull the hour from the “From” line
by finding the time string and then splitting that string into parts using
the colon character. Once you have accumulated the counts for each
hour, print out the counts, one per line, sorted by hour as shown below.

python timeofday.py
Enter a file name: mbox-short.txt
04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1
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
    word=line[5]
    w=word.split(":")
    y=w[0]
    d[y]=d.get(y,0)+1
l = list(d.keys())
l.sort()
for item in l:
    print(item,d.get(item))
        

"""
A very interesting exercise. With very few minor changes we have a completely diffent program.
Those change include, line38, where we take the 6th word, separating that into a list of words via ":" (line39)
we take the hours(line 40), we fill the dictionary with that key and the number of times it appears as its value(line 41)
we fill up the list with the keys of the dictionary(line42), we sort that list(line 43) and lastly for every item in that list
we print that item along its value form the dictionary)(line 44-45)
"""