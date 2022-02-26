#Write down a program which recognizes whether the inserted word is a palindrome or not.

word=input("Please insert a word:\n")
arithmos=-1
palindrome=""
while arithmos>-len(word)-1:
    anapodos=word[arithmos]
    palindrome=palindrome+anapodos
    arithmos=arithmos-1
if word==palindrome:
    print("The above word is palindrome")
else:
    print("The above word is not a palindrome")


