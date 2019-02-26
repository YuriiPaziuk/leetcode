"""
Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root: return []
        paths = []

        def find(root, path=''):
            if not root.left and not root.right: paths.append(path + str(root.val))
            if root.left: find(root.left, path + str(root.val) + '->')
            if root.right: find(root.right, path + str(root.val) + '->')

        find(root)
        return paths


def main():
    root = TreeNode(11)
    root.left = TreeNode(22)
    root.right = TreeNode(33)
    root.left.left = TreeNode(44)
    print(Solution().binaryTreePaths(root))


if __name__ == '__main__':
    main()
