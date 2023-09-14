def aStarAlgo(start_node, stop_node):
    open_set = set(start_node)
    closed_set = set()
    g = {}
    parents = {}

    g[start_node] = 0

    parents[start_node] = start_node
    while len(open_set) > 0:
        n = None

        for v in open_set:
            if n == None or g[v] + heuris
                n = v
        if n == stop_node or Graph_nodes[
            pass
        else:
            for (m, weight) in get_neighb

                if m not in open_set and 
                    open_set.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight

                else:
                    if g[m] > g[n] + weig
                        #update g(m)
                        g[m] = g[n] + wei

                        parents[m] = n

                        if m in closed_se
                            closed_set.re
                            open_set.add(
        actual_cost = g[m]
        if n == None:
            print('Path does not exist!')
            return None


        if n == stop_node:
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start_node)
            path.reverse()
            actual_cost += heuristic(stop
            print('Path found: {}'.format
            print('Actual cost = ',actual
            print("ESTIMATED COST = ",heu
            if actual_cost < heuristic (s
                print ('Path Admissible')
            else :
                print('Path NOT Admissibl

            return path

        open_set.remove(n)
        closed_set.add(n)
    print('Path does not exist!')
    return None


def get_neighbors(v):
    if v in Graph_nodes:
        return Graph_nodes[v]
    else:
        return None

def heuristic(n):
    H_dist = {
        'S': 11.5,
        'A': 10.1,
        'B': 5.8,
        'C': 3.4,
        'D': 9.2,
        'E': 7.1,
        'F': 3.5,
        'G': 0,

    }
    return H_dist[n]

Graph_nodes = {
    'S': [('A', 3), ('D', 4)],
    'A': [('D', 5), ('B', 4), ('S', 3)],
    'D': [('A', 5), ('E', 2), ('S', 4)],
    'B': [('A', 4), ('E', 5), ('C', 4)],
    'E': [('D', 2), ('B', 5), ('F', 4)],
    'F': [('E', 4), ('G', 3.5)],
    'C': [('B', 4)],
    'G': [('F', 3.5)],
}

S = input("Enter Start Node:\n")
G = input("Enter Goal Node:\n")
aStarAlgo(S,G)
