class Solution(object):
    def isBalanced(self, root):
        def dfsHeight(root):
            if root is None:
                return 0
            leftHeight = dfsHeight(root.left)
            if leftHeight == -1:
                return -1
            rightHeight = dfsHeight(root.right)
            if rightHeight == -1:
                return -1
            if abs(leftHeight - rightHeight) > 1:
                return -1
            return max(leftHeight, rightHeight) + 1
        
        return dfsHeight(root) != -1


