counting=0
athroisma=0         #defining the counter, sum , and median variables at the begining in order to be included in the loop
mesos_oros=0

while True:
    try:
        
        dedomeno=input("Please insert a valid number:\n") #Requesting from the user to enter their input(number preferably)
        if dedomeno=="Done": #if the user enters the word "Done", then we shall proceed out of the loop.
            break
        counting=counting+1    #since we defined counting as 0, every time we insert an input it should be raised by 1
        athroisma=athroisma+int(dedomeno)   #since we defined athroisma as 0, every time we insert a new input, the sum of the number entered is calculated
    except:
        print("The input you have entered is not recognized, please try again.") #if the user inserts an input different that a number or the word "Done", they shall meet the message below, again requiring from them to continue inserting their inputs
        continue
    
    
mesos_oros=athroisma/counting #since we require the counting and athroisma values to be collected, we further define mesos_oros, outside the loop.
print("The total of inputs entered is:",counting)
print("The total of sum ofthe inputs entered is:",athroisma)
print("The median of the inputs entered is:",mesos_oros)



#I had a huge problem with this one, originally I defined the input as an floating number, since I was expecting the
#user to insert numbers. However, doint the word "string" "Done", could not be processed leading directly to the except clause.
#I tried removing the float from the input, but then every number i inserted was seen as a string value, hence the
#the program was not delivering. However, by identifying the input variable (dedomeno),below the "Done" clause,
#I was able to complete the assignment. That was a headacke.