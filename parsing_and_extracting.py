# from envans.doni@gmail.com received from his lover's iphone on the 24th of December 2021.


data= "from envans.doni@gmail.com received from his lover's iphone on the 24th of December 2021"
papaki= data.find("@")  #tracking where the designated letter is located in the text.
print(papaki)
kenaki=data.find(" ",papaki)    #starting from the position we traced the abovementioned letter find the next space.
print(kenaki)
host=data[papaki+1 : kenaki]    #since the starting order starts from 0 we add 1 to that syntaxtd with a colomn (:) up until but not included the positioned of the second traced variable.
print(host)
poutsaki=data.find(".",papaki)  #I was asked to try to shorten the research up until the domain, without the suffix.  Easily done.
vantsgay=data[papaki+1: poutsaki]
print(vantsgay)