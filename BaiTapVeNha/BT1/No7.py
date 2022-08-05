# Exercise 1: Reverse a current_list in Python

def ReverseList(Input_List):
    reverse_result = []
    index = len(Input_List) - 1
    while index >= 0:
        reverse_result.append(Input_List[index])
        index += -1
    print(reverse_result)


# Exercise 2: Concatenate two lists index-wise
def Concatenate(list1, list2):
    list_result = []
    for i in range(len(list1)):
        list_result.append(list1[i] + list2[i])
    print(list_result)


# Exercise 6: Remove empty strings from the current_list of strings
def RemoveEmptyElement(ListElement):
    for element in ListElement:
        if element == "":
            ListElement.remove(element)

    print(ListElement)


# Exercise 9: Replace current_list’s item with new value if found
def replace_elementList(current_list, value_need_replace, New_value):
    no_value_need_replace = current_list.count
    while value_need_replace in current_list:
        index_target = current_list.index(value_need_replace)
        current_list[index_target] = New_value
    print(current_list)
