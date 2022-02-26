onoma=input("Please eneter a file name:")
try:
    kappa=open(onoma, "r")
except:
    print("The name you have entered is not valid...")
boulouki=0
count=0
for line in kappa:
    if line.startswith("X-DSPAM-Confidence:"):
        count=count+1
        koulouri=float(line[19:]) #or if we had identified another variable as the lenght of the quoted phrase, we could have used that as the first item in the sliced bracket.
        boulouki=koulouri+boulouki
print("Average spam confidence:",boulouki/count) 

#line1:We prompt the user to enter a file name, prettry straighforward.
#line2-5: In case the user enters an invalid file name, we use the try and except safeguard to inform the user about their incorrect input.
#line6-7: We indentify outisde the loop our two variables.
#line8: We introduse a for loop on the lines of the file.
#line9: Every time the file starts with the quoted line, our counter will increase.
#line11: We identify the lenght of the lines that start with the quoted phrase and then we slice the line to include only the numerical part.
#line12: We add to that the two variables.
#line13: We print the final text, outside the loop, we wish to be showed.