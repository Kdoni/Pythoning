from re import A


def computegrade(Kappa):
    if Kappa >=0.9 and Kappa<=1:
        return "A"
    elif Kappa >=0.8:
        return "B"
    elif Kappa >=0.7:
        return "C"
    elif Kappa >=0.6:
        return "D"
    elif Kappa <0.6:
        return "You failed this class"
    else:
        return "Please insert an appropriate value"
try:
    grade = float(input("Please insert your grade:\n"))
    
except:
    print("Please insert an appropriate value:")
    exit()
if grade >1 and grade!=float:
    print("Please insert and appropriate value:")
    exit()
print (computegrade(grade))
