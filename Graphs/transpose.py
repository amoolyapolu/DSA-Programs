class Graph:
  def __init__(self,v):
    self.v = v
    self.adj_matrix = [[0 for i in range(v)] for j in range(v)]
  def add_edge(self,s,d):
    self.adj_matrix[s][d] = 1
    self.adj_matrix[d][s] = 1
  def transpose_matrix_inplace(self): # inplace will reduce the space complexity from creating an extra matrix to doing on the original one
    self.adj_matrix = [[self.adj_matrix[j][i] for j in range(self.v)]for i in range(self.v)]
  def display_matrix(self):
    for row in self.adj_matrix:
            print(row)


if __name__ == "__main__":
    # Initialize an adjacency matrix with 4 vertices
    graph = Graph(5)

    # Add some edges to the graph
    graph.add_edge(0, 1)
    graph.add_edge(0, 3)
    graph.add_edge(2, 0)
    graph.add_edge(3,2)
    graph.add_edge(4,1)
    graph.add_edge(4,3)
    

    # Display original adjacency matrix
    print("Original Adjacency Matrix:")
    graph.display_matrix()

    # Transpose the graph in-place
    graph.transpose_matrix_inplace()

    # Display transposed adjacency matrix
    print("\nTransposed Adjacency Matrix:")
    graph.display_matrix()
