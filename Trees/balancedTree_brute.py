class Tree:
  def __init__(self,val):
    self.val = val
    self.left = None
    self.right = None
    
  def isBalanced(self,root):
    if self.root is None:
      return True
    left_height = self.get_height(root.left)
    right_height = self.get_height(root.right)

    if abs(left_height - right_height) <= 1 and \
           self.isBalanced(root.left) and \
           self.isBalanced(root.right):
      return True
  def get_height(self,root):
    # Recursively calculate the height
        # of left and right subtrees
        left_height = self.getHeight(root.left)
        right_height = self.getHeight(root.right)

        # Return the maximum height of left and right subtrees
        # plus 1 (to account for the current node)
        return max(left_height, right_height) + 1
