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
if __name__ == "__main__":
    # Initialize an adjacency matrix with 4 vertices
    graph = Graph(4)

    # Add some edges to the graph
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 3)
    graph.display_adj_matrix()
    
for vertex in range(graph.num_vertices):
    print(f"Degree of vertex {vertex}: {graph.get_degree(vertex)}")
