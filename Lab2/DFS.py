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
        elif s not in graph or graph[s] is []:
            continue
        for (neighbour, value) in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                stack.push(neighbour)


def dfsRoad(graph, start, end):
    print("In duong di:")
    visited = []  # List to keep track of visited nodes.
    stack = ImplementStack.Stack()
    stack.push(start)
    parents = {}
    path = []
    parents[start] = start
    while stack.data:
        # get the first path from the stack
        # print(f'visited: {visited}')
        path.append(stack.pop())
        # print(f'path: {path}')
        # get the last node from the path
        node = path[-1]
        visited.append(node)
        # path found
        if node == end:
            print(f'DFS parent{parents}')
            return path
        if node not in graph:
            continue
        # enumerate all adjacent nodes, construct a new path and push it into the queue
        for (neighbour, value) in graph.get(node, []):
            if neighbour not in visited:
                # visited.append(neighbour)
                new_path = list(path)
                parents[neighbour] = node
                new_path.append(neighbour)
                for key in new_path:
                    if key not in stack.data:
                        stack.push(key)


def RunDFS(Note, Grab, Start, End):
    print(f'Chay do thi theo giai thuat DFS{Note}')
    print(dfsRead(Grab, Start, End))
    print(dfsRoad(Grab, Start, End))
    print("--------------------")
