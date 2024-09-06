class Node:
    def __init__(self, val):
        # Initialize a node with a given value and set its children to None
        self.data = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        # Initialize an empty binary search tree
        self.root = None

    def insert(self, val):
        # Insert a value into the BST
        new_node = Node(val)
        # If the tree is empty, set the new node as the root
        if self.root is None:
            self.root = new_node
            return
        
        # Otherwise, find the correct position for the new node
        current = self.root
        parent = None
        
        while current is not None:
            parent = current
            if val < current.data: 
                # Move to the left if the value is smaller than the current node
                current = current.left
            else:
                # Move to the right if the value is greater than the current node
                current = current.right

        # Insert the new node as a left or right child based on its value
        if val < parent.data:
            parent.left = new_node
        else:
            parent.right = new_node

    def search_recursive(self, root, val):
        # Recursively search for a value in the tree
        if root is None or root.data == val:
            # Return the node if it's found, or None if not found
            return root
        
        if val < root.data:
            # Search in the left subtree if the value is smaller
            return self.search_recursive(root.left, val)
        # Search in the right subtree if the value is larger
        return self.search_recursive(root.right, val)

    def search_iterative(self, val):
        # Iteratively search for a value in the tree
        current = self.root
        while current:
            if current.data == val:
                # If the value is found, return True
                return True
            elif val < current.data:
                # Move to the left if the value is smaller
                current = current.left
            else:
                # Move to the right if the value is greater
                current = current.right
        # Return False if the value is not found
        return False

    def delete(self, root, val):
        # Helper function to find the minimum value in a subtree
        def find_min(node):
            while node.left is not None:
                node = node.left
            return node

        if root is None:
            # Return None if the tree is empty or the value is not found
            return root

        # Traverse the tree to find the node to be deleted
        if val < root.data:
            root.left = self.delete(root.left, val)
        elif val > root.data:
            root.right = self.delete(root.right, val)
        else:
            # Node with only one child or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            
            # Node with two children: Get the in-order successor (smallest in the right subtree)
            temp = find_min(root.right)
            # Replace the node's data with the in-order successor's data
            root.data = temp.data
            # Delete the in-order successor
            root.right = self.delete(root.right, temp.data)

        # Return the modified tree
        return root

    def delete_node(self, val):
        # Delete a node with the given value from the tree
        self.root = self.delete(self.root, val)
      
if __name__ == "__main__":
    bst = BST()

    # Insert nodes into the BST
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(2)
    bst.insert(7)
    bst.insert(12)
    bst.insert(20)

    # Print the root and some child nodes to verify insertion
    print(f"Root: {bst.root.data}")
    print(f"Left child of root: {bst.root.left.data}")
    print(f"Right child of root: {bst.root.right.data}")

    # Search for some values recursively and iteratively
    print("\nSearch for 7 recursively:", bst.search_recursive(bst.root, 7) is not None)
    print("Search for 12 iteratively:", bst.search_iterative(12))
    print("Search for 100 (nonexistent) iteratively:", bst.search_iterative(100))

    # Delete some nodes
    bst.delete_node(7)  # Delete a leaf node
    print("\nDeleted node 7. Search for 7:", bst.search_recursive(bst.root, 7) is not None)

    bst.delete_node(15)  # Delete a node with one child
    print("\nDeleted node 15. Search for 15:", bst.search_recursive(bst.root, 15) is not None)

    bst.delete_node(10)  # Delete the root node (node with two children)
    print("\nDeleted root node (10). New root:", bst.root.data)

