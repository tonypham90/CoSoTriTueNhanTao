# Exercise 1: Add a list of elements to a set
def AddListElementToASet(Dict_List, NewElementList):
    for New_element in NewElementList:
        Dict_List.update({New_element})
    print(Dict_List)


# Exercise 5: Remove items from the set at once
def Remove_Multiple_Value(SetList, MultipleValue):
    SetList.difference_update(MultipleValue)
    print(SetList)


# Exercise 9: Remove items from set1 that are not common to both set1 and set2
def TakeSameValueInBothSet(Dict1, Dict2):
    Dict1.intersection_update(Dict2)
    print(Dict1)
