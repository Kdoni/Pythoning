"""
Exercise 6: Rewrite the program that prompts the user for a list of
numbers and prints out the maximum and minimum of the numbers at
the end when the user enters “done”. Write the program to store the
numbers the user enters in a list and use the max() and min() functions to
compute the maximum and minimum numbers after the loop completes.
Enter a number: 6
Enter a number: 2
Enter a number: 9
Enter a number: 3
Enter a number: 5
Enter a number: done
Maximum: 9.0
Minimum: 2.0
"""

lista=[]    #Setting an empty list out of the loop to use later.
while True: #Commencing a while true loop, to keep asking for inputs, or show the error message, until the break is utilised.
    inp=input("Enter a number: ")
    if inp=="done":     
        break
    try:
        x=float(inp)
    except:
        print("Please try entering a number....")
        continue
    lista.append(x)
print("Maximum:",max(lista))
print("Minimum:",min(lista))      


"""At my fist try, I attempted to initiallize the guardian try/except combo, even after the initial input request
I came to the conclusion that this was counterintuitive. If I was requesting for a float number, then even the word "done", would have been caught at the 
except. Seems fairly easy to comprehend now, but it was a bit challenging to come up with setting another variable that would only accept the float inputs
and using that as the try safeguard.
The rest were pretty straighforward. 
Once more, there is a huge difference between the indented lista and the unidented one.
The first, being in the loop, will keep adding items in the list, the other, will only add the last input
"""