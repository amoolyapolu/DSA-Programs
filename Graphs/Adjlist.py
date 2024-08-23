
class Graph:
    def __init__(self,num_nodes,directed = True):
        self.directed = directed
        self.num_nodes = num_nodes
        self.m_list_of_edges = []
    def add_edge(self,n1,n2,weight):
        self.m_list_of_edges.append([n1,n2,weight])
        if not self.directed:
            self.m_list_of_edges.append([n2,n1,weight])
    def print_edge_list(self):
        num_edges = len(self.m_list_of_edges)
        for i in range(num_edges):
            print("edge ", i+1, ": ", self.m_list_of_edges[i])
graph = Graph(5)

graph.add_edge(0, 0, 25)
graph.add_edge(0, 1, 5)
graph.add_edge(0, 2, 3)
graph.add_edge(1, 3, 1)
graph.add_edge(1, 4, 15)
graph.add_edge(4, 2, 7)
graph.add_edge(4, 3, 11)
graph.print_edge_list()
        
