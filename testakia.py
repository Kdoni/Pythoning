#Write a program which counts how many time a letter is written in a word or sentence.



#Solving the questinon with a for loop.
x=("How many a's, does this sentence have?:\n")
counter=0
for letter in x:
    if letter=="a":
        counter=counter+1
print("The above mentioned sentece/word, has",counter,"words")


#Solving the question with a while loop:

x=("How many a's, does this sentence have?\n")
arithmos=0
counter=0
while arithmos<len(x):
    y=x[arithmos]
    if y=="a":
        counter=counter+1
    arithmos=arithmos+1
print(counter)
