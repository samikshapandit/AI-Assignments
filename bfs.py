from queue import Queue


def bfs(graph, start, Goal):
    visited = list()  # to keep track of visited nodes
    queue = Queue()  # initialize queue
    queue.put(start)  # add the starting node to queue

    while not queue.empty():
        node = queue.get()  # get the next node from the queue

        if node not in visited:
            visited.append(node)  # mark node as visited
            if (node == Goal):
                print("Goal: " + node + " found")
                break
            else:
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        queue.put(neighbor)

            # add unvisited neighbors of node to queue

    print(visited)


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': [],
    'D': [],
    'E': [],

}

bfs(graph, 'A', 'D')