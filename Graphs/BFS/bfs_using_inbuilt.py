from collections import deque

def BFS(ajlist,s,vis):
  q=deque()
  vis[s]=True
  q.append(s)
  while q:
    curr_node=q.popleft()
    # print("curr_nde")
    print(curr_node,end=" ")
    for neigh in ajlist[curr_node]:
    #   print("neigh",end="\n")
    #   print(neigh)
      if not vis[neigh]:
        vis[neigh]=True
        q.append(neigh)
        
def addEdge(ajlist,u,v):
  ajlist[u].append(v)

def main():
  v = 5
  ajlist = [[] for _ in range(v)]
  addEdge(ajlist,0,1)
  addEdge(ajlist,0,2)
  addEdge(ajlist,1,3)
  addEdge(ajlist,1,4)
  addEdge(ajlist,2,4)
  vis= [False]*v
  print("BFS")
  BFS(ajlist,0,vis)

if __name__ == "__main__":
  main()
  
