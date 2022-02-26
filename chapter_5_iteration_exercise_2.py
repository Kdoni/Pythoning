maximum_number=float("-inf") #Defining the maximum number as negative infinitum, meaning that every other number should be larger than this one.
minimum_number=float("inf")     #Defining the minimjm number as infinitum, meaning that every other number should be larger than this one.
while True: #Using this opener for a while in order to proceed into an ifinite loop, until instructed otherwise.
    try: #I attempted to catch invalid input with the try/except clause.
        dedomeno=input("Please insert a valid number:\n") #Prompting the user to insert inputs, preferably numbers.
        if dedomeno=="Done": #When the user enters this specific word the loop shall be exited.
            break
        elif int(dedomeno)>maximum_number:      #In this one I had to define dedomeno, twice as integers.Initially I did not do that and only one number was regarded as a number, from the second and onwards everynumber was considered a string.
            maximum_number=int(dedomeno)
            continue
        elif int(dedomeno)<minimum_number:
            minimum_number=int(dedomeno)
            continue
    except:
        print("Invalid input!")
print("The maximum number entered is:",maximum_number)
print("The minimum number entered is:",minimum_number)



#After having already completed a similar assignment, I still had problems with this one.
#I believe I got the hand of the try and except clause in order to "catch" potential faulty inputs.
#I am still not confident in the distinction between if, elif and else. Apparently, if and else is a duality, while 
#elif is an additionla scenario without disregarding the others.
#The catch was not to initally define the permissable values of dedomeno in order to allow all potential values to be
#proccessed. Next in the scenarios where the variable was supposed to be a number, define the variable on the spot.
#Moreover, I am still not entirely confident on the while true opener.