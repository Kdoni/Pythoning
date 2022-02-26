def computepay(h, r):
    if h<=40:
        return h*r
    else:
        return (h-40)*(0.5*r) +(h*r)
hrs = float(input("Enter Hours:\n"))
rate = float(input("Enter Rate:\n"))
p = computepay(hrs,rate)
print("Pay", p)