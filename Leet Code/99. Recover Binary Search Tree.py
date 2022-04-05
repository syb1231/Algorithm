# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        
        self.temp = []
        def dfs(node):
            if not node :return
            dfs(node.left)
            self.temp.append(node)
            dfs(node.right)
        dfs(root)
        srt = sorted(n.val for n in self.temp)
        for i in range(len(srt)):
            self.temp[i].val = srt[i]
            
 # 순회 개념 부족 
