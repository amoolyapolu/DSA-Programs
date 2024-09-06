def in_order_helper(self, node):
    if node is not None:
        # First, recursively visit the left subtree
        self.in_order_helper(node.left)
        
        # Then, visit (print) the current node
        print(node.data, end=" ")
        
        # Finally, recursively visit the right subtree
        self.in_order_helper(node.right)
def inorder(self):
  self.in_order_helper(self.root)
  print()

def pre_order_helper(self,node):
  if node is not None:
        # First, visit (print) the current node
        print(node.data, end=" ")
        # Then recursively visit the left subtree
        self.pre_order_helper(node.left)
        # Finally, recursively visit the right subtree
        self.pre_order_helper(node.right)

def preorder(self):
  self.pre_order_helper(self.root)
  print()

def post_order_helper(self,node):
  if node is not None:
        
        # First recursively visit the left subtree
        self.post_order_helper(node.left)
        # then, recursively visit the right subtree
        self.post_order_helper(node.right)
        # Finally, visit (print) the current node
        print(node.data, end=" ")

def postorder(self):
  self.post_order_helper(self.root)
  print()
