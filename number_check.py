'''
Cinthya Calderon-Hernandez
CMSC 111
Spring 2026
Assignment 3: Number Check
'''

#Ask user for a nymber and make it a float
number = float(input("Enter a number: "))

#Check if number is postive, negative, or zero
if number > 0:
    print("Your number is positive!")
elif number < 0:
    print("Your number is negative!")
else:
    print("Your number is zero!")
