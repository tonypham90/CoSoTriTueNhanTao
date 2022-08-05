# Exercise 1: Convert two lists into a dictionary
def ConvertListToDict(Keys_list, Values_list):
    dict_result = {}
    for i in range(len(Keys_list)):
        dict_result[Keys_list[i]] = Values_list[i]
    print(dict_result)


# Exercise 4: Initialize dictionary with default values
def CreateNewElementWithDefaultValue(Keys_list, Default):
    dictlist = dict.fromkeys(Keys_list, Default)
    print(f'This is result: {dictlist}')


# Exercise 5: Create a dictionary by extracting the keys from a given dictionary
def GetDictInfByListKey(Dict, Key_list):
    dict_inf = {}
    for key in Key_list:
        dict_inf[key] = Dict[key]
    print(dict_inf)


# Exercise 7: Check if a value exists in a dictionary
def IsValuePresentInDict(Dict, Value_check):
    for value in Dict:
        if Dict[value] == Value_check:
            return print(f'Value {Value_check} present in the Dict')
    print(f"The Value {Value_check} doesn't present in the Dict")
