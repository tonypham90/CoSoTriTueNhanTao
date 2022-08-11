class GraphData:
    def __init__(self):
        self.adjacency_list = {}
        self.heuristic = {}
        self.heuristicSub = {None}
        self.Name = ''


DoThi1 = GraphData()
DoThi1.Name = 'Do Thi 1'
DoThi1.adjacency_list = {
    'S': [('A', 2), ('F', 3), ('B', 1)],
    'F': [('G', 6)],
    'A': [('C', 2), ('D', 3)],
    'C': [('G', 4)],
    'D': [('G', 4)],
    'B': [('D', 2), ('E', 4)],
    'E': [],
    'G': []
}
DoThi1.heuristic = {
    'S': 6,
    'A': 4,
    'B': 5,
    'C': 2,
    'D': 2,
    'E': 8,
    'F': 4,
    'G': 0

}
DoThi2 = GraphData()
DoThi2.Name = "Do Thi 2"
DoThi2.adjacency_list = {
    's': [('f', 1), ('h', 1)],
    'f': [('p', 1)],
    'h': [('k', 1)],
    'k': [('c', 1)],
    'p': [('q', 1)],
    'c': [('a', 1)],
    'q': [('r', 1)],
    'r': [('t', 1)],
    't': [('g', 1)],
    'a': [('b', 1)],
    'b': [('d', 1)],
    'd': [('m', 1), ('e', 1)],
    'e': [('n', 1)],
    'n': [('m', 1)],
    'm': [('g', 1)],
    'g': [('m', 1), ('t', 1)]
}
DoThi2.heuristic = {
    's': 4,
    'f': 5,
    'h': 3,
    'k': 2,
    'p': 4,
    'c': 3,
    'q': 3,
    'r': 2,
    't': 1,
    'a': 4,
    'b': 3,
    'd': 2,
    'e': 3,
    'n': 2,
    'm': 1,
    'g': 0

}
DoThi3 = GraphData()
DoThi3.Name = "Do Thi 3"
DoThi3.adjacency_list = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 1), ('D', 5)],
    'C': [('B', 1), ('D', 3)],
    'D': [('E', 8), ('G', 9), ('F', 5)],
    'E': [('G', 2)],
    'F': [('G', 5)],
    'G': [('D', 9), ('E', 2), ('F', 5)]
}
DoThi3.heuristic = {
    'A': 9.5,
    'B': 9,
    'C': 8,
    'D': 7,
    'E': 1.5,
    'F': 4,
    'G': 0
}
DoThiMau = GraphData()
DoThiMau.Name = "Do Thi Mau"
DoThiMau.adjacency_list = {
    'A': [('B', 1), ('C', 3), ('D', 7)],
    'B': [('D', 5)],
    'C': [('D', 12)],
    'D': []
}
DoThiMau.heuristic = {
    'A': 1,
    'B': 1,
    'C': 1,
    'D': 1
}
DoThi4 = GraphData()
DoThi4.Name = 'Do Thi 4'
DoThi4.adjacency_list = {
    'Arad': [('Zerind', 75), ('Sibiu', 140), ('Timisoara', 118)],
    'Zerind': [('Oradea', 71), ('Arad', 75)],
    'Oradea': [('Sibiu', 151), ('Zerind', 71)],
    'Timisoara': [('Lugoj', 111), ('Arad', 118)],
    'Lugoj': [('Mehadia', 70), ('Timisoara', 111)],
    'Mehadia': [('Dobreta', 75), ('Lugoj', 70)],
    'Dobreta': [('Craiova', 120), ('Mehadia', 75)],
    'Sibiu': [('Rimnicu Vilcea', 80), ('Fagaras', 99), ('Oradea', 115), ('Arad', 140)],
    'Fagaras': [('Bucharest', 211), ('Sibiu', 99)],
    'Bucharest': [('Fagaras', 211), ('Pitesti', 101), ('Urziceni', 85), ('Giurgiu', 90)],
    'Rimnicu Vilcea': [('Sibiu', 80), ('Craiova', 146), ('Pitesti', 97)],
    'Craiova': [('Dobreta', 120), ('Rimnicu Vilcea', 146), ('Pitesti', 138)],
    'Pitesti': [('Rimnicu Vilcea', 97), ('Bucharest', 101), ('Craiova', 138)],
    'Giurgiu': [('Bucharest', 90)],
    'Neamt': [('Iasi', 87)],
    'Iasi': [('Neamt', 87), ('Vaslui', 92)],
    'Vaslui': [('Iasi', 92), ('Urziceni', 142)],
    'Urziceni': [('Vaslui', 142), ('Bucharest', 85), ('Hirsova', 98)],
    'Hirsova': [('Urziceni', 98), ('Eforie', 86)],
    'Eforie': [('Hirsova', 86)]
}
DoThi4.heuristic = {
    'Arad': 366,
    'Zerind': 374,
    'Oradea': 380,
    'Timisoara': 329,
    'Lugoj': 244,
    'Mehadia': 241,
    'Dobreta': 242,
    'Sibiu': 253,
    'Fagaras': 178,
    'Bucharest': 0,
    'Rimnicu Vilcea': 193,
    'Craiova': 160,
    'Pitesti': 98,
    'Giurgiu': 77,
    'Neamt': 234,
    'Iasi': 226,
    'Vaslui': 199,
    'Urziceni': 80,
    'Hirsova': 151,
    'Eforie': 161
}
