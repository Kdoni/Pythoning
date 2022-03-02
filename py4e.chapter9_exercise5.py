"""
Exercise 5: This program records the domain name (instead of the
address) where the message was sent from instead of who the mail came
from (i.e., the whole email address). At the end of the program, print
out the contents of your dictionary.
python schoolcount.py
Enter a file name: mbox-short.txt
{'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}
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
    domain=word.split("@")
    w=domain[1]
    d[w]=d.get(w,0)+1
print(d)
    
    
    
#This exercise was simply asking to split the email into a list separated by "@", take the 2nd part and add that
#to a dictionary along with how many times that 2nd part appears.
