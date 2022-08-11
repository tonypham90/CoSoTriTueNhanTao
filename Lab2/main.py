# This is a sample Python script.
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from collections import OrderedDict

import Graph_data
from Astar2 import Graph as Astar
from Greedy import Graph as Greedy
from UCS import Graph as UCS
from Graph_data import DoThi4
from Graph_data import DoThi1
from Graph_data import DoThi2
from Graph_data import DoThi3
from DFS import RunDFS as DFS


class run_Graph:
    def __init__(self):
        self.Graph = Graph_data.GraphData()
        self.Start = ''
        self.Goal = ''

    def Get_Graph(self, GraphData, Start, Goal):
        self.Graph = GraphData
        self.Start = Start
        self.Goal = Goal

    def run_Graph(self):
        print(f"--------------------------------------/\n"
              f"Tim duong {self.Graph.Name} tu {self.Start} den {self.Goal}")
        print(f'Method: A*')
        graph_astar = Astar(self.Graph.adjacency_list, self.Graph.heuristic)
        graph_astar.a_star_algorithm(self.Start, self.Goal, self.Graph.Name)
        print(f'Method UCS')
        graph_astar = UCS(self.Graph.adjacency_list, self.Graph.heuristic)
        graph_astar.a_star_algorithm(self.Start, self.Goal, self.Graph.Name)
        print(f'Method Greedy')
        graph_astar = Greedy(self.Graph.adjacency_list, self.Graph.heuristic)
        graph_astar.a_star_algorithm(self.Start, self.Goal, self.Graph.Name)
        print(f'Method: DFS')
        DFS(self.Graph.Name, self.Graph.adjacency_list, self.Start, self.Goal)


if __name__ == '__main__':
    # DoThiMau_Run_Astar = Astar(DoThiMau.adjacency_list, DoThiMau.heuristic)
    # DoThiMau_Run_Astar.a_star_algorithm('A', 'D')
    print("Co So Tri Tue Nhan Tao"
          "\nBai Tap Lap2: UCS, GREEDY va A* setup"
          "\n Sinh Vien Pham Tuan Anh\n"
          "MSSV: 21880005\n")
    # Create opject run graph

    RunDoThi1 = run_Graph()
    RunDoThi2 = run_Graph()
    RunDoThi3 = run_Graph()
    RunDoThi4 = run_Graph()
    RunDoThi1.Get_Graph(DoThi1, 'S', 'G')
    RunDoThi1.run_Graph()
    RunDoThi2.Get_Graph(DoThi2, 's', 'g')
    RunDoThi2.run_Graph()
    RunDoThi3.Get_Graph(DoThi3, 'A', 'G')
    RunDoThi3.run_Graph()
    RunDoThi4.Get_Graph(DoThi4, 'Arad', 'Bucharest')
    RunDoThi4.run_Graph()

    # print(min(DoThi1.heuristic, key=DoThi1.heuristic.get))
    # DFS(DoThi1.Name, DoThi1.adjacency_list, 'S', 'G')

    # a = [('A', 2), ('F', 3), ('B', 1)]
    # a.insert(0, ('K', 9))
    #
    # print(a)
    # print(a[0][0])
