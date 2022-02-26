count=0
total=0
while True:
    arithmoi=input("Please insert a number:")
    if arithmoi=="Done":
        break
    try:
        value=int(arithmoi)
        total=total+value
        count=count+1
    except:
        print("Vale arithmous roufiane...")
        continue
average=total/count
print("The average is:",average)

#line1-2: First of all we define the variables we would like to base our program on.
#line3: We use a while True statement in order for the program to keep askings us for an input.
#line5-6: When we insert a certain keyword the, we break outside of the loop and go to the next lines.
#line7-13: We apply a try and except guard in order to safeguard against potential misinputs.
#line14: With continue, the program goes back to the beginning of the loop to keep asking us for our inputs.



#Personal notes: I believe I got the hang of the While true concept, the break and continue.
#Try and except is pretty straighforward to me now. I managed to write down this program, pretty much on my own.