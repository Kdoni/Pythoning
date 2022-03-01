while True:
    fname=input("Please insert a file name:")
    try:
        handle=open(fname,"r")
        break
    except:
        print("The file name you have entered is not valid...")
        continue

"""A pretty standart approach to requesting the user to enter their input
A while True to start an indefinate loop, until we fulfil the try guardian code in order to break out of the loop.
And an except to request from the user to enter another input, notifying them of the inability to perform the task
"""

counts=dict()
for line in handle:
    words=line.split()
    for word in words:
        counts[word]=counts.get(word,0)+1


"""A very eloquent way to proceed to solve this hurdle with dictionaries.
First we set up the dictionary, then in a for loop, we break the lines into lists. Afterwards for every item in the list we add to the dictionary the number of times it has appeared.
"""
#In this case, three words appear the same ammount of times as the most used'

wordcount=0
morethan1list=[]
for word,count in counts.items():
    if count > wordcount:
        morethan1list.clear()
        morethan1list.append(word)
        wordcount=count
    elif count==wordcount:
        morethan1list.append(word)
        
"""In these lines of code, I made some changes. I noticed that, if the most common word, happens to be more than 1, the program will one show the first one
hence, I decided to construct a list to add the words which also have the same ammount of appearences with an elif statement.
I believe I made this a bit better, still it was pretty challenging to come up with this answer.
"""

print(wordcount,*morethan1list)

#If you use"*" in front of a list, the result will be a bit more presentable.