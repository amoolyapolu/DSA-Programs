"""
Given an undirected graph with V vertices and E edges and a node X, 
The task is to find the level of node X in the undirected graph. If X does not exist in the graph then return -1.
Input: V = 5, Edges = {{0, 1}, {0, 2}, {1, 3}, {2, 4}}, X = 3
Output: 2
"""
from collections import deque

def bfs(adj_list, start,k):
    level = [0] * len(adj_list)
    visited = [False] * len(adj_list)
    
    q = deque()
    q.append(start)
    level[start] = 0
    visited[start] = True

    while q:
        p = q.popleft()

        for neighbor in adj_list[p]:
            if not visited[neighbor]:
                level[neighbor] = level[p] + 1
                q.append(neighbor)
                visited[neighbor] = True
    
    return level[k]

# Example usage:
adj_list = [[1, 2], [0, 3], [0, 4], [1], [2]]
start_vertex = 0
levels = bfs(adj_list, start_vertex,3)
print("Levels of nodes:", levels)
