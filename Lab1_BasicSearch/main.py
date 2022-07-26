# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
import BFS
import Graph

if __name__ == '__main__':
    print(BFS.bfsNoRoad(Graph.SAMPLE1, "A", "G"))
    print(BFS.bfsWithRoad(Graph.SAMPLE2, "1", "11"))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
