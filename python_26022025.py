'''
https://www.w3schools.com/python/python_operators.asp


Data types:
string = "hello word"
integer = 10
float = 10.5
boolean = True

Data structures:
tuple = (1,2,3,4,5)
Set = {1,2,3,4,5}
dictionary = {"name": "John", "age": 30}
list = [1,2,3,4,5]

x = "10"
y = "20"
z = x + y
=> z = "1020" Concatenation

x = 10
y = 20
z = x + y
=> z = 30 Concatenation


Conditions:
If ... else
While loop
for loop

Functions:
To perform certain tasks
'''

# Variables
# x = input("Enter a number: ")
# y = input("Enter another number: ")
# operation = input("Enter the operation: ")

# if operation == "+":
#     z = int(x) + int(y)
#     print(z)
# elif operation == "-":
#     z = int(x) - int(y)
#     print(z)
# elif operation == "*":
#     z = int(x) * int(y)
#     print(z)
# elif operation == "/":  
#     z = int(x) / int(y) 
#     print(z)
# else:
#     z = "Invalid operation"
#     print(z)

# n = input("Enter a number: ")
# n = int(n)

# while n < 5:
#     n = n + 1
#     if n%2 == 0:
#         print("The value is less than 5")
#         continue

# x = [1,2,3,4,5,6]
# for value in x:
#     print(2 * value)

def calculator(num1, num2, operation):
    if operation == "+":
        z = int(num1) + int(num2)
        return z
    elif operation == "-":
        z = int(num1) - int(num2)
        return z
    elif operation == "*":
        z = int(num1) * int(num2)
        return z
    elif operation == "/":  
        z = int(num1) / int(num2) 
        return z
    else:
        z = "Invalid operation"
        return z

number = calculator(3,4,'+')
print(number + 2)