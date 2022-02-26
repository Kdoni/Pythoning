def computepay(Hours, Rate):
    if hours<=40:
        return Hours*Rate
    elif hours>40:
        return ((hours-40)*0.5*rate) + Hours*Rate
    
try:
    hours= float(input("Please insert your working hours:\n"))
except:
    print("Please insert an appropriate value:")
    exit()
if hours<0:
    print("Please insert an appropriate value:")
    exit()
try:
    rate = float(input("Please insert your hourly rate:\n"))
    if rate<0:
        print("Please insert an appropriate value:")
        exit()
except:
    print("Plese insert an appropriate value:")
    exit()
salary = computepay(hours,rate)
print(salary)