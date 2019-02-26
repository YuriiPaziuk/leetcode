"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary
tree in which the depth of the two subtrees of every node never differ by more than 1.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root):
        """
        Bottom up approach, O(n)
        :type root: TreeNode
        :rtype: bool
        """
        def height(root):
            """Return height of the tree if the tree is height-balanced,
            -1 if the tree is not height-balanced"""
            if not root: return 0

            left_height = height(root.left)
            if left_height == -1: return -1

            right_height = height(root.right)
            if right_height == -1: return -1

            if abs(left_height - right_height) > 1: return -1

            return max(left_height, right_height) + 1

        return height(root) != -1



    def isBalanced1(self, root):
        """Top down approach, O(n^2)"""
        def height(root):
            if not root: return 0
            else: return max(height(root.left), height(root.right)) + 1

        if not root: return True

        current_balanced = abs(height(root.left) - height(root.right)) <= 1
        left_balanced = self.isBalanced1(root.left)
        right_balanced = self.isBalanced1(root.right)
        return current_balanced and left_balanced and right_balanced


def main():
    #root = None
    root = TreeNode(11)
    root.left = TreeNode(22)
    #root.right = TreeNode(33)
    root.left.left = TreeNode(44)
    print(Solution().isBalanced(root))


if __name__ == '__main__':
    main()
