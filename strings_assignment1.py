text="X-DSPAM-Confidence:          0.8475"
envans=text.find(".")
pente=text.find("5")
poutsa=text[envans-1:len(text)]
print(float(poutsa))   

#After careful consideration, instead of trying to track down the singular number 5, we could have instead tried to measure the lenght (len) of the whole varialbe (text) and then print the space between the number prior to the "." and the whole lenght of the variable.