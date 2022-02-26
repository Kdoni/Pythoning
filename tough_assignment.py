bigaf= float("-inf")
smallaf= float("inf")
while True:
        dedomeno=input("Please insert a valid input:")
        if dedomeno =="done":
                break
        try:
                arithmos =int(dedomeno)
        except:
                print("Invalid Number")
                continue
        if arithmos>bigaf:
                bigaf=arithmos
        if arithmos<smallaf:
                smallaf=arithmos
print(bigaf,smallaf)
        

