def bfsRead(graph, start, end):
    print("In cac nut duoc duyet qua:")
    visited = []  # List to keep track of visited nodes.
    queue = []  # Initialize a queue
    visited.append(start)
    queue.append(start)

    while queue:
        s = queue.pop(0)
        print(s, end=" ")
        if s == end:
            return
        elif s not in graph:
            continue
        else:
            for neighbour in graph[s]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)


def bfsRoad(graph, start, end):
    print("In duong di:")
    visited = []  # List to keep track of visited nodes.
    queue = [[start]]  # Initialize a queue
    # maintain a queue of paths
    # push the first path into the queue
    while queue:
        # get the first path from the queue
        path = queue.pop(0)
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
                queue.append(new_path)


def RunBFS(Note, Grab, Start, End):
    print(Note)
    print(bfsRead(Grab, Start, End))
    print(bfsRoad(Grab, Start, End))
    print("--------------------")
