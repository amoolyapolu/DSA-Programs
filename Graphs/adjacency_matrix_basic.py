print("Try programiz.pro")
v=3
edges = [(0, 1), (1, 2), (2, 0)]
l=[]
l=[[0 for i in range(v)] for j in range(v)]
print(l)
def add_edge(l,edges):
    for e in edges:
       x,y=e
       l[x][y]=1
       l[y][x]=1
    return l
print(add_edge(l,edges))
