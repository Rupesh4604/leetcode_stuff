# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        stack = [(root, 0)]
        total_sum = 0
        
        while stack:
            node, current_sum = stack.pop()
            current_sum = current_sum * 10 + node.val
            
            if not node.left and not node.right:
                total_sum += current_sum
            else:
                if node.right:
                    stack.append((node.right, current_sum))
                if node.left:
                    stack.append((node.left, current_sum))
        
        return total_sum

# class Solution:
#     def sumNumbers(self, root: Optional[TreeNode]) -> int:
#         def dfs(node, current_sum):
#             if not node:
#                 return 0
#             # Update the current sum by shifting digits and adding the current node's value
#             current_sum = current_sum * 10 + node.val
#             # If it's a leaf node, return the current sum
#             if not node.left and not node.right:
#                 return current_sum
#             # Otherwise, continue the depth-first search
#             return dfs(node.left, current_sum) + dfs(node.right, current_sum)
        
#         return dfs(root, 0)
