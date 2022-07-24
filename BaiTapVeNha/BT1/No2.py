# Exercise 1: Accept numbers from a user
# Write a program to accept two numbers from the user and calculate multiplication
def ImportNumberfromUser():
    print("Multiple 2 numer:")
    first_number = int(input("Your first number:"))
    second_number = int(input("Your second number:"))
    print(f"{first_number} * {second_number} = {first_number * second_number}")


# Exercise 4: Display float number with 2 decimal places using
def formatNumberWithInput(number):
    # float(number)
    print(f'the Number before format {number}. After format {format(float(number), "0.2f")}')


# Exercise 5: Accept a list of 5 float numbers as an input from the user
def Input5floatNumber():
    print("Input 5 value one by one:")
    list_number = []
    for i in range(5):
        list_number.append(float(input(f"value No {i + 1}:")))
    print(f"result is {list_number}")

#     Exercise 7: Accept any three string from one input() call
def SeprateNamebyInput():
    print("Please input all list name and seprate by comma',':")
    stringNamelist = input("List Name:")
    list = stringNamelist.split(",")
    for i in range(len(list)):
        print(f"Name {i+1}:{list[i]}")
