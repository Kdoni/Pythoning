#Write a program, which prompts the user and then writed their reply in reverse order, in the same line.


pitsoulis=input("Pes mou ena frouto:\n")
arithmos=-1
klanias=""
while arithmos>-len(pitsoulis)-1:
    mikros=pitsoulis[arithmos]
    klanias=klanias+mikros
    arithmos=arithmos-1
print(klanias)


#It was extremely difficult and done with outside help, of thinking of naming (blank) a seperate variable, outside the loop.
#It was also very difficult to come out with de indending the print outside of the loop, for it to showcase a single line.
#Overall it is mostly the same with a simple program of writting a word in reverse order, but it was very important to keep in mind the first two points.
