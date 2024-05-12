class adjNode:
  def __init__(self,node):
    self.node=node
    self.next = None

class Graph:
  def __init__(self,vertices):
    self.v=vertices
    self.adj_list = [None] * self.v

  def addedge(self,s,d):
    node = adjNode(d)
    node.next = self.adj_list[s]
    self.adj_list[s] = node
    # print(self.adj_list)
    
  def display_graph(self):
    for i in range(self.v):
      print(i,end=" ")
      temp=self.adj_list[i]
      while temp:
        print("->", temp.node, end=" ")
        temp = temp.next
      print("\n")
  def add_vertex(self):
        self.v += 1
        self.adj_list.append(None)
      
if __name__ == "__main__":
 
    V = 6
    graph = Graph(V)
    graph.addedge(0, 1)
    graph.addedge(0, 3)
    graph.addedge(0, 4)
    graph.addedge(1, 2)
    graph.addedge(3, 2)
    graph.addedge(4, 3)
 
    print("Initial adjacency list")
    graph.display_graph()
    
    print("Add vertex")
    graph.add_vertex()
    graph.display_graph()
 
