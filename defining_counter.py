def count(tzatziki,giaourti):
    counter=0
    for miksa in giaourti:
        if miksa==tzatziki:
            counter=counter+1
    return(counter)



word="Karapoutsara"
print(count("r",word))


#That was actually hard.