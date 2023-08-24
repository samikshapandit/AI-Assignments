def bfs(matrix , n , start):
    visited = [False] * n
    q = []
    q.append(start)
    visited[start] = True
    while q:
        vis = q.pop(0)
        print(vis)

        if vis == goal:
            break;

        for node in range(0 , n):
            if matrix[vis][node] == 1 and not visited[node]:
                q.append(node)
                visited[node] = True

if __name__ == "__main__":
    n = int(input("Enter number of nodes : "))
    matrix = []
    print("Enter adjacency matrix\n")
    for i in range(n):
        a = []
        for j in range(n):
            a.append(int(input()))
        matrix.append(a)

    start = int(input("Enter starting vertex : "))

    goal = int(input("Enter goal node"));

    bfs(matrix , n , start)
