import random

# ROLLING DICE

throw="y"
print("----------------------------------------")
print("Throw The DICE")
print("----------------------------------------")
while throw.lower()=="y":
    print(random.randint(1,6))
    throw=input("Enter 'y' if you want to throw dice again: ")
print("----------------------------------------")
print("Thanks for throwing dice")
print("----------------------------------------")