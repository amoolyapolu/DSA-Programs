class AdjNode:
    def __init__(self, data):
        self.vertex = data
        self.next = None


class AdjList:
    def __init__(self, vertices):
        self.v = vertices
        self.graph = [None] * self.v

    def addedge(self, source, destination):
        print("source",source,"V",self.v)
        if source >= self.v or destination >= self.v or source < 0 or destination < 0:
            print(f"Error: Vertex out of bounds. Source: {source}, Destination: {destination}")
            return
        
        # Check if the edge already exists to avoid duplicates
        temp = self.graph[source]
        while temp:
            if temp.vertex == destination:
                print(f"Edge already exists between {source} and {destination}")
                return
            temp = temp.next

        # Add the edge from source to destination
        node = AdjNode(destination)
        node.next = self.graph[source]
        self.graph[source] = node

    def addvertex(self, vk, source, destination):
        if vk >= self.v or source >= self.v or destination >= self.v or vk < 0 or source < 0 or destination < 0:
            print(f"Error: Vertex out of bounds. vk: {vk}, Source: {source}, Destination: {destination}")
            return

        self.addedge(source, vk)
        self.addedge(vk, destination)

    def print_graph(self):
        for i in range(self.v):
            print(f"Vertex {i}:", end="")
            temp = self.graph[i]
            while temp:
                print(f" -> {temp.vertex}", end="")
                temp = temp.next
            print()

    def delvertex(self, k):
        if k >= self.v or k < 0:
            print(f"Error: Vertex {k} does not exist.")
            return

        # Remove all edges to the vertex k
        for i in range(self.v):
            prev = None
            temp = self.graph[i]
            while temp:
                if temp.vertex == k:
                    if prev:
                        prev.next = temp.next
                    else:
                        self.graph[i] = temp.next
                    temp = None
                else:
                    prev = temp
                    temp = temp.next

        # Remove all edges from the vertex k
        self.graph[k] = None


# Driver code
if __name__ == "__main__":
    V = 6
    graph = AdjList(V)

    # Adding edges
    graph.addedge(0, 1)
    graph.addedge(0, 3)
    graph.addedge(0, 4)
    graph.addedge(1, 2)
    graph.addedge(3, 2)
    graph.addedge(4, 3)
    

    print("Initial adjacency list")
    graph.print_graph()

    # Adding an existing edge (should be handled)
    graph.addedge(0, 1)

    # Adding an edge with an out-of-bounds vertex (should be handled)
    graph.addedge(0, 6)

    # Add vertex
    graph.addvertex(5, 3, 2)
    print("\nAdjacency list after adding vertex")
    graph.print_graph()

    # Attempt to delete a non-existing vertex (should be handled)
    graph.delvertex(7)

    # Delete vertex
    graph.delvertex(4)
    print("\nAdjacency list after deleting vertex")
    graph.print_graph()
