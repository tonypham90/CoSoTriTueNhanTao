# Exercise 1: Print First 10 natural numbers using while loop
def print_first_number_lower_input_number(MaxNumber):
    print(f"Print all number lower than {MaxNumber}")
    int(MaxNumber)
    i = 1
    while i <= MaxNumber:
        print(i)
        i += 1


# Exercise 2: Print the following pattern
def PrintPattern(TargetNumber):
    print("PrintPattern Number")
    int(TargetNumber)
    i = 1
    while i <= TargetNumber:
        list_number = []
        r = 1
        while r <= i:
            list_number.append(r)
            r += 1
        print(list_number)
        i += 1


# Exercise 4: Write a program to print multiplication table of a given number
def Print_Multiplication_firstTenNumber(Number):
    int(Number)
    for i in range(10):
        print(Number * i)


# Exercise 5: Display numbers from a current_list using loop
def PrintGoodNumber(ListNumber):
    for i in range(len(ListNumber)):
        if ListNumber[i] > 500:
            return
        elif ListNumber[i] % 5 == 0 and ListNumber[i] <= 150:
            print(ListNumber[i])
