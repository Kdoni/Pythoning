# Figure out which line of the above program is still not
# properly guarded. See if you can construct a text file which causes the
# program to fail and then modify the program so that the line is properly
# guarded and test it to make sure it handles your new text file.

fhand = open('mbox.txt')
for line in fhand:
    words = line.split()
# print('Debug:', words)
    if len(words) == 0:
        continue
    if words[0] != 'From':
# If the 0th word is indeed From, but not an email address...., print the third word would be meaningless.
        continue
    if len(words)!=7:
        continue
    print(words[2])

#Summary: That was indeed a headache.
#Thinking what could possibly go wrong is the essence of programming.
#A first thought came to contain the spread of searc by signaling (if len(words)<3), continue. 
#Meaning that if the elements in a list are less than 3, continue searching.
#Why 3? Because at the end we signal the program to print the 3rd element. Removing potential lines, starting with "From" with less than 3 lines to influencec the program.
#After more thought, I though it was more proactive to continue searching only lines with exact 7 elements, seeing that a common demoninator of the emails is the 7 mark.
#Hopefully it does a better job safeguarding the program.