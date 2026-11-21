# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # def dfs(root):
        #     if not root:
        #         return

        #     root.left, root.right = root.right, root.left

        #     dfs(root.left)
        #     dfs(root.right)

        # dfs(root)
        # return root

        # if not root:
        #     return None
        # stack = [root]

        # while stack:
        #     curr = stack.pop()
        #     curr.left, curr.right = curr.right, curr.left
        #     if curr.left:
        #         stack.append(curr.left)
        #     if curr.right:
        #         stack.append(curr.right)

        # return root
        if not root:
            return None
        q = deque([root])

        while q:
            curr = q.popleft()
            curr.right, curr.left = curr.left, curr.right
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)

        return root




        