vis = []
def DFS(u,adj):
    vis[u] = True
    for v in adj[u]:
        if vis[v] != True:
            DFS(v,adj)
            
def printResult(res):
    for i in range(len(res)):
        print(i, "->", end=" ")
        for j in res[i]:
            print(j, end=" ")
        print()

def solve(n,edges):
    adj_list_rev = [[] for i in range(n)]
    for i in range(len(edges)):
        u, v = edges[i][0], edges[i][1]
        adj_list_rev[v].append(u)
    res = [[] for i in range(n)]
    for i in range(n):
        vis.clear()
        vis.extend([False] * n)
        DFS(i, adj_list_rev)
        arr = []
        for j in range(n):
            if vis[j] and i != j:
                arr.append(j)
                
        res[i] = arr
    printResult(res)
    
if __name__ == "__main__":
    N = 5
    Edges = [[0, 4], [4, 1], [4, 3], [1, 2]]

    # Function Call
    solve(N, Edges)
