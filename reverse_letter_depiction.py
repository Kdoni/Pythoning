#Write a program which prompts the user for their input and writes that back in reverse order.


mikroulis=input("Please insert a word:\n")
arithmos=-1
while arithmos>-len(mikroulis)-1:
    anapodos=mikroulis[arithmos]
    print(anapodos)
    arithmos=arithmos-1