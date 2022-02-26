onoma=input("Pleae enter a file name:")
if onoma=="Gazpoutso":
    print("You've been gnomed")
    exit()
try: 
    kappa=open(onoma, "r")
    
except:
    print("The file name you have entered is not valid...")
    exit()
count=0
for line in kappa:
    line=line.rstrip()
    if len(line)>0:
        count=count+1
print("There were",count,"subject lines in",onoma)

#line1: Prompting the user to insert a file name.
#line2-4: We start with an if statement to properly set in place the easter egg. That was a pretty tricky one, because is set into the try,
#then both the easter egg message and the incorrect message will be shown.
#Overall, the rest was pretty straighforward.
#Always keep in mind the positioning of all the orders.