numlist=list()
while True:
    inp=input("Please enter a number:")
    if inp=="Done":
        break
    try:
        value=float(inp)
    except:
        print("Artithmous vre cringe :D")
        continue
    numlist.append(value)
average=sum(numlist)/len(numlist)
print("The average is:",average)


#A very nice way to construct a simple median code with lists.
#Step one: We create a list. Then a new variable is the float equavalent of the inputs. Then we add that variable at the list and keep addind, this is where the while true statement helps out.
#Last, we construct a new variable which is the sum of the numbers entered (sum) divided by the lenght (len) meaning the number of numbers inserted. Pretty cool.
