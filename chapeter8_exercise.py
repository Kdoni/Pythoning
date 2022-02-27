#Exercise 1: Write a function called chop that takes a list and modifies
# it, removing the first and last elements, and returns None. Then write
# a function called middle that takes a list and returns a new list that
# contains all but the first and last elements.

x=[1,2,3,4,5,6,7,8,9,10]
def chop(x):
    del x[0]
    del x[len(x)-1]

def middle(x):
    t=x[1:len(x)-1]   
    return(t)
    
a=middle(x)
print(a)
print(x)

#It was a great challenge.
#Line1: construct a basic list.
#Line2-4: Defining the function. Deliting the 0th position, meaning the first element, and the last (lenght of the list-1).
#There is no reason to return since the modifications are happening on the above provided list.
#Line 5-7: Defining the second function. We start by setting up a new variable to include the 2nd element(1st) up to, but not including the last.
#We return the new variable (return(t)). If we did not return, the function would not have worked.


#Difference between, (pop), (remove), (del):

#(pop)

# t = ['a', 'b', 'c']
# x = t.pop(1)
#  print(t)
# ['a', 'c']
#  print(x)
# b

#(del)

# t = ['a', 'b', 'c']
# del t[1]
# print(t)
# ['a', 'c']

#(remove)

# If you know the element you want to remove (but not the index), you can use
# remove:

# t = ['a', 'b', 'c']
# t.remove('b')
# print(t)
# ['a', 'c']