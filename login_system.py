'''
Cinthya Calderon-Hernandez
CMSC 111
Spring 2026
Assignment 2: Perimeter of a Rectangle
'''

#Statement of correct username and password
correct_username = "cool_cinthya"
correct_password = "beanscool"

#Ask for credentials
username = input("Enter your username: ")
password = input("Enter your password: ")

#Check if login info is correct
if username == correct_username and password == correct_password:
    print("Login successful!")
else:
    print("Login failed. Incorrect username or password.")