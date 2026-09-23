# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        def kth(root,k):
            if not root:
                return 
            kth(root.left,k)
            res.append(root.val)
            kth(root.right,k)
        kth(root,k)
        return res[k-1]