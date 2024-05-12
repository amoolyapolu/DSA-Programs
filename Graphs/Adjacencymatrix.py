class Graph:
  def __init__(self,num_of_vertices):
    self.num_vertices = num_of_vertices
    self.adj_matrix= [[0 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
    
  def add_edge(self,u,v):
      self.adj_matrix[u][v]=1
      self.adj_matrix[v][u]=1
      
  def display_adj_matrix(self):
    for i in (self.adj_matrix):
      print(i)
      
  def get_degree(self,vertex):
      return sum(self.adj_matrix[vertex])

  def addVertex(self):
    self.num_vertices=self.num_vertices+1
    for row in self.adj_matrix:
        row.append(0)

    # print(self.adj_matrix)
    
    self.adj_matrix.append([0]*self.num_vertices)
  def removeVertex(self,vertex):  
    if vertex>=self.num_vertices:
        print("cant remove")
        return
    
    else:
        while vertex<self.num_vertices-1:
            for i in range(0,self.num_vertices):
                self.adj_matrix[i][vertex] = self.adj_matrix[i][vertex+1]
            for j in range(0,self.num_vertices):
                self.adj_matrix[vertex][j] = self.adj_matrix[vertex+1][j]
            vertex=vertex+1
        for row in self.adj_matrix:
            row.pop()
        self.adj_matrix.pop()
        self.num_vertices = self.num_vertices-1
  
        
        
if __name__ == "__main__":
    # Initialize an adjacency matrix with 4 vertices
    graph = Graph(4)

    # Add some edges to the graph
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 3)
    # graph.display_adj_matrix()
    graph.addVertex()
    graph.display_adj_matrix()
    print("removing vertex")
    graph.removeVertex(1)
    graph.display_adj_matrix()
for vertex in range(graph.num_vertices):
    print(f"Degree of vertex {vertex}: {graph.get_degree(vertex)}")
