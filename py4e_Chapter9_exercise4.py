"""
Exercise 4: Add code to the above program to figure out who has the
most messages in the file. After all the data has been read and the dictionary has been created, look through the dictionary using a maximum
loop (see Chapter 5: Maximum and minimum loops) to find who has
the most messages and print how many messages the person has.
Enter a file name: mbox-short.txt
cwen@iupui.edu 5
Enter a file name: mbox.txt
zqian@umich.edu 195
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
for key,value in d.items():
    w=max(d.values())
    if value==w:
        print(key,w)



#line26: I decided to initiate a for loop for both the keys and the values in the dictionary(d.items)
#line27: I constructed a new variables which will be the maximum of the values of the dictionary(probably not necessary)
#line28-29: If the value is the maximum value then print its key.

"""
Took some thought, I had to brass through my notes, but when I rememberd I could run through both keys and values 
in a dictionary, it was plain sailing.
"""
