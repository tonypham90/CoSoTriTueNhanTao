# Exercise 1: Create a list by picking an odd-index items from the first list and even index items from the second
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
