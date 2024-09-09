# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
class TreeNode:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
        
def max_depth(root):
       
        if not root:
            return 0
        queue = [root]
        depth = 0
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth += 1
        return depth
        
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print(max_depth(root))  # Output: 3


                
