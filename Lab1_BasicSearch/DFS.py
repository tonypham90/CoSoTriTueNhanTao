import ImplementStack


def dfsRead(graph, start, end):
    print("In cac nut duoc duyet qua:")
    visited = []  # List to keep track of visited nodes.
    stack = ImplementStack.Stack()
    visited.append(start)
    stack.push(start)

    while stack.data:
        s = stack.pop()
        print(s, end=" ")
        if s == end:
            return
        elif s not in graph:
            continue
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                stack.push(neighbour)


def dfsRoad(graph, start, end):
    print("In duong di:")
    visited = []  # List to keep track of visited nodes.
    stack = ImplementStack.Stack()
    stack.push(start)
    while stack.data:
        # get the first path from the stack
        path = stack.pop()
        # get the last node from the path
        node = path[-1]
        # path found
        if node == end:
            return path
        # enumerate all adjacent nodes, construct a new path and push it into the queue
        for neighbour in graph.get(node, []):
            if neighbour not in visited:
                new_path = list(path)
                new_path.append(neighbour)
                stack.push(new_path)


def RunDFS(Note, Grab, Start, End):
    print(Note)
    print(dfsRead(Grab, Start, End))
    print(dfsRoad(Grab, Start, End))
    print("--------------------")
