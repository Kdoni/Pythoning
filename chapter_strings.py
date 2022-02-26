from argparse import BooleanOptionalAction


# fruit= "banana"
# letter=fruit[1]
# print (letter)
# x=3
# w=fruit[x-1]
# print (w)

# fruit="Bananitsa"
# x=len(fruit)
# print(x)

# fruit="banana" #Simply defining the variable "fruit"
# index=0        #Since an array starts from 0, we define the "index" as being 0
# while index<len(fruit): #While the new variable "index", being larger than the lenght of the variable (loop)    Moreover the lenght of the variable is 6 letters, hence when the variable index, reaches 6 the condition of index being smaller than len(fruit) will not apply.
#     letter=fruit[index] # The new variable "letter" equals the first letter of the variable fruit [], starting from 0
#     print(index,letter) #The letter 0 will be shown, since we defined this varible as 0, along with the first letter of the variable.
#     index=index+1 #Then the variable index will change its value and the loop will continue until all the letters of the variable have been covered, ending the loop.

# fruit="Banana" #Defining the variable
# for letter in fruit: # A definite  loop with for . 
#     print (letter)

# word="Banana"     #Defining the variable
# count=0             #definiting the other variable, we choose 0 to help us on the next steps to properly make the additions
# for letter in word:     #starting a loop with the letters in the variable using the for definite loop
#     if letter=="a":     #if any of the letters has the value of a, then add 1.
#         count=count+1   #adding all the a's until all the letters of the varialbe have been examined.
# print(count)        #Print the final results, which is the sum of a's until all the letter have been examined.


s="Monty Python"
print(s[0:4]) #from 0 up to 4, not including 4
print(s[6:7])
print(s[6:29])