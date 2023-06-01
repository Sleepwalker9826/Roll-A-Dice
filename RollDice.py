import random
import time
Name=input("Please Enter Your Name : ")
print("Hello", Name)
loop = True
while loop:
    Q1=input("Want to roll the dice? (y/n) : ")
    if Q1 == "y":
        print("Rolling...")
        time.sleep(1)
        print("You rolled ", random.randint(1,6))
    elif Q1 == "n":
        loop = False