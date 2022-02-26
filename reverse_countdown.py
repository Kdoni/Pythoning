from time import sleep

while True:
    try:
      x=int(input("Please choose how many seconds you wish to live :D:"))
      while x>0:
        print(x)
        x=x-1
        sleep(1)
    except:
        print("Please insert a valid value!")
        continue
    break
print("Kalo paradeiso :D")