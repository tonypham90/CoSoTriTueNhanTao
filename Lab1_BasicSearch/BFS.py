visited = []  # List to keep track of visited nodes.
queue = []  # Initialize a queue


def bfsNoRoad(visited, graph, start, end):
    visited.append(start)
    queue.append(start)
    while queue:
        s = queue.pop(0)
        print(s, end=" ")
        if s == end:
            return
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


def bfsWithRoad(graph, start, end):
# maintain a queue of paths
    visited = []
    queue = []

    # push the first path into the queue
    queue.append([start])
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
