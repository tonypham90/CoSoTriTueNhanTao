# Exercise 1A: Create a string made of the first, middle and last character


def string_first_middle_last(string):
    middle = int(len(string) / 2)
    text = string[0] + string[middle] + string[-1]
    print(text)


"a".isnumeric()


# Exercise 5: Count all letters, digits, and special symbols from a given string
def Counterintelligence(string):
    no_symbol = 0
    no_alpha = 0
    no_digit = 0
    for letter in string:
        if letter.isnumeric():
            no_digit += 1
            continue
        else:
            if ord(letter) < 64 or (91 < ord(letter) < 96) or ord(letter) > 123:
                no_symbol += 1
                continue
            else:
                no_alpha += 1
    print(f'No of Symbol = {no_symbol}\n'
          f'No of Alphal = {no_alpha}\n'
          f'No of Digit = {no_digit}')


# Exercise 10: Write a program to count occurrences of all characters within a string
def CountUniqLetter(String):
    list_result = {}
    for letter in String:
        if letter not in list_result:
            list_result[letter] = [String.count(letter)]

    print(list_result)


# Exercise 13: Split a string on hyphens
def Split_String(String, SymbolSplit):
    list_result = String.split(SymbolSplit)
    for element in list_result:
        print(element)
