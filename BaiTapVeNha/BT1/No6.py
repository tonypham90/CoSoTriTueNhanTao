# Exercise 1: Create a current_list by picking an odd-index items from the first current_list and even index items from the second
def mixList(firstList, SecondList):
    odd_list = []
    even_list = []
    third_list = []
    j = 1
    for i in range(len(SecondList)):
        if i % 2 == 0:
            even_list.append(SecondList[i])
    while j < len(firstList):
        odd_list.append(firstList[j])
        j += 2
    for i in odd_list:
        third_list.append(i)
    for i in even_list:
        third_list.append(i)

    print(f"Element at odd-index positions from list one\n{odd_list}")
    print(f'Element at even-index positions from list two\n{even_list}')
    print(f'Printing Final third list\n{third_list}')


# Exercise 2: Remove and add item in a current_list
def RemoveAndAddElement(ListNumber):
    print(f'Original list {ListNumber}')
    element = ListNumber.pop(4)
    print(f'After remove element at index 4{ListNumber}')
    ListNumber.insert(2, element)
    print(f'After adding element at index 2 {ListNumber}')
    ListNumber.append(element)
    print(f'After add element at the last position of the list {ListNumber}')


# Exercise 6: Find the intersection (common) of two sets and remove those elements from the first set
def FindAndSetUnique(firstList, secondList):
    print(f"print {firstList}")
    intersection_list = firstList.intersection(secondList)
    for element in intersection_list:
        firstList.remove(element)
    print(f'Intersection is {intersection_list}')
    print(f'first set after remove comment: {firstList}')


# Exercise 8: Iterate a given current_list and check if a given element exists as a key’s value in a dictionary. If not, delete it from the current_list

def Doublecheck(listElement):
    list_unique = []
    for element in listElement.values():
        if element not in list_unique:
            list_unique.append(element)
    print(f'Result: {list_unique}')
