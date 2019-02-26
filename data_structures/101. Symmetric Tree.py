"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True

        from queue import deque

        left_queue = deque()
        right_queue = deque()

        left_queue.append(root.left)
        right_queue.append(root.right)

        while left_queue and right_queue:

            left = left_queue.pop()
            right = right_queue.pop()

            if not left and not right: continue
            if not left or not right: return False
            if left.val != right.val: return False

            left_queue.append(left.left)
            right_queue.append(right.right)

            left_queue.append(left.right)
            right_queue.append(right.left)

        return True
