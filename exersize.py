fruit="Banana"
index=-1
while index>-len(fruit)-1:
    envans=fruit[index]
    print(envans)
    index=index-1

#In this program we try to write the variable in reverse order. Each letter at a time.
#To do that, first we have to define the variable.
#Then we define a variable as -1, which would signal the last letter of the variable.
#Afterwards, in a while loop, if certain conditions are met, until all the letters have been read(in this case the -1 has to be larger than the negative lenght of the variable's word -1).
#Then a new variable would be the bracketed number of the first variable.
#Lastly, we signal the showing of the results of the new variable, in the first instance it shall be the last character of the variable's value.
#And last, make the value of the indeded number to be decreased by 1, that would change the original value of the new variable, and so on, until all the letter have been read, meaning the conditions signaled at the indefinate loop (while).