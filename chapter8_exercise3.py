# Exercise 4: Find all unique words in a file
# Shakespeare used over 20,000 words in his works. But how would you
# determine that? How would you produce the list of all the words that
# Shakespeare used? Would you download all his work, read it and track
# all unique words by hand?
# List all unique words, sorted
# in alphabetical order, that are stored in a file romeo.txt containing a
# subset of Shakespeare’s work.
# Create a list of unique words, which will contain the final result. Write
# a program to open the file romeo.txt and read it line by line. For each
# line, split the line into a list of words using the split function. For
# each word, check to see if the word is already in the list of unique
# words. If the word is not in the list of unique words, add it to the list.
# When the program completes, sort and print the list of unique words
# in alphabetical order.

"""
Exercise 4: Find all unique words in a file
Shakespeare used over 20,000 words in his works. But how would you
determine that? How would you produce the list of all the words that
Shakespeare used? Would you download all his work, read it and track
all unique words by hand?
List all unique words, sorted
in alphabetical order, that are stored in a file romeo.txt containing a
subset of Shakespeare’s work.
Create a list of unique words, which will contain the final result. Write
a program to open the file romeo.txt and read it line by line. For each
line, split the line into a list of words using the split function. For
each word, check to see if the word is already in the list of unique
words. If the word is not in the list of unique words, add it to the list.
When the program completes, sort and print the list of unique words
in alphabetical order.
"""
while True:     #I used the while True loop in order to continually prock the user's input in case the file name is not met.
    inp=input("Please insert a file name:")
    try:        #If the file name is successfuly met, then break out of the loop and continue below.
        x=open(inp,"r")
        break
    except:
        print("The file name you have entered is not valid...")
        continue    #If the file name is not met, continue, meaning keep asking the user to input their input.
count=0
listfin=[]
listall=[]
for line in x:
    list1=line.split()  #Up to this point the program breaks the text into separate lists with the words of each line as the items in the list.
    listall=listall+list1[0:]   #Now, by defining a separe variable as an empty list we add that empty list to each character of the separate lists, making a new list with all the items.
    listall.sort()  #sorting the list into alphabetical order.
#Up to this point everything works fine.
for word in listall:
    y=listall[count]        #I kept on thinking of removing items form the already sorted list. After a few hours scratching my head I decided that this was
    count=count+1           #not the only possible solution. In the end I decided to make a new list, to include items from the sorted list with one restriction,
    if y not in listfin:    #If the item is not in the empty list, add it to the list, meaning that words that are reapeted will not, but for the first, be included in the list.
        listfin.append(y)   #A very challeging, yet enjoying exercize.
        continue
print(listfin)
    
    
    
    

        