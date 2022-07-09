# Exercise 1: Calculate the multiplication and sum of two numbers Given two integer numbers return their product only
# if the product is equal to or lower than 1000, else return their sum.

def SumOrMultiple(firstNumber, secondNumber):
    if firstNumber * secondNumber <= 1000:
        return firstNumber + secondNumber
    else:
        return firstNumber * secondNumber


# Exercise 2: Print the sum of the current number and the previous number. Write a program to iterate the first 10
# numbers and in each iteration, print the sum of the current and previous number.

def PrintSumCurrentAndPreviousNumber(Number):
    sum_number = 0
    previous_number = 0
    print(f'Print current Number and Previous Number Sum in a range({Number})')
    for i in range(Number):
        current_number = i
        sum_number = current_number + previous_number
        print(f'The Current Number is {current_number}, the Previous Number is {previous_number}, Sum: {sum_number}')
        previous_number = current_number


