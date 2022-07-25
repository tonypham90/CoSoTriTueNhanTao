# Exercise 2: Create a function with variable length of arguments

def printallAgumentinput(*Value):
    print("Print All Value:")
    for Number in Value:
        print(Number)


# Exercise 3: Return multiple values from a function
def Caculate2Number(a, b):
    addition = a + b
    substraction = a - b
    multiple = a * b
    device = a / b
    return addition, substraction, multiple, device


# Exercise 4: Create a function with default argument
# Write a program to create a function show_employee() using the following conditions.
#
# It should accept the employee’s name and salary and display both.
# If the salary is missing in the function call then assign default value 9000 to salary
def show_employee(Name, Salary=9000):
    print(Name, Salary)
