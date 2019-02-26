"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        from collections import deque
        q = deque()
        q.append((root, 1))
        while q:
            current, depth = q.popleft()
            if not current.left and not current.right: return depth
            if current.left: q.append((current.left, depth + 1))
            if current.right: q.append((current.right, depth + 1))


def main():
    root = None
    root = TreeNode(11)
    root.left = TreeNode(22)
    root.right = TreeNode(33)
    root.left.left = TreeNode(44)
    root.right.left = TreeNode(55)
    print(Solution().minDepth(root))


if __name__ == '__main__':
    main()
