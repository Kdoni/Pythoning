
try:
    hours= float(input("Πόσες ώρες εργαστήκατε;\n"))
    money= float(input("Ποιό είναι το ωρομίσθιό σας;\n"))
    if hours<=40:
        print(f"Τα χρήματα που δικαιούστε είναι:\n{hours*money}")
    else:
        print(f"Τα χρήματα που δικαιούστε είναι:\n{(hours*money)+((hours-40)*0.5*money)}")
        print("\n\n\n\nΕυχαριστούμε για την παροχή της ελευθερίας σας :).")
except:
    print("Βρε μπαγλαμά, βάλε νούμερα...")
exit()
