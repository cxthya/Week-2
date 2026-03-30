'''
Cinthya Calderon-Hernandez
CMSC 111
Spring 2026
Assignment 1: Variables and Data Types
'''

#Ask for user information
name = input("Enter your name: ")
age = int(input("Enter your age: "))
pi_value = float(input("Enter the value of pi: "))
is_human = input("Are you human? (True/False): ") == "True"

#Make to a complete sentence 
print(f"My name is {name}, I am {age} years old, the value of pi is {pi_value}, and it is {is_human} that I am human.")