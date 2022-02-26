fhand=open("mbox-short.txt","r")
for line in fhand:
    line=line.strip()
    if len(line)>0:
        print(line.upper())