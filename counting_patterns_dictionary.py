counts=dict()   #First step: Create a dictionary.
print("Enater a line of text: ")    
line=input("")  #Empty input, we type whatever we like.
words=line.split()  #We make a list of the words we typed, each word is a list element, separate by space.
print("Words: ",words)  #We print that list.
print("Counting...")
for word in words:  #Initiating a definite for loop.
    counts[word]=counts.get(word,0)+1   #The dictionay"counts" with key "word", is the dictionary.get(word,0)+1, meaning that if a word alrady exists, add one if not make it 1.
print("Counts",counts)