# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
1. First go to left till the left node. 
2. The left leaf node will be the left tail and the right leaf node will be the right tail.
3. Point the left tail's right wot the root's right
    root's right to the root's left
    and root's left to the null
4. We also have to keep a note of the last node of the LinkedList. Therefore, if the right of root is not None, the it will be the last node. 
    If both right and left of root are none then root will be the last node.
    Else if only right is None then left will be the last node
'''
#Time Complexity: O(n)
#Space Compledity: O(h)
class Solution(object):
    def dfs(self, root):
        #You need to return the tail of the left subtree
        
        #Edge case
        if not root:
            return None

        #Recurse
        leftTail=self.dfs(root.left)
        rightTail=self.dfs(root.right)
        
        #That is if the left subtree exists
        if root.left is not None:
            leftTail.right=root.right
            root.right=root.left
            root.left=None
        
        if not rightTail and not leftTail:
            lastTail=root
        elif not rightTail:
            lastTail=leftTail
        else:
            lastTail=rightTail
            
        return lastTail
            
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.dfs(root)
