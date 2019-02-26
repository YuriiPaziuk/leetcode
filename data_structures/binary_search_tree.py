class BinarySearchTreeNode:

    def __init__(self, key, val=None):
        self.key = key
        self.val = val
        self.left = None
        self.right = None


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def size(self):
        pass

    def is_empty(self):
        return self.size() == 0

    def get(self, key):
        return self._get(key, self.root)

    def _get(self, key, node):
        pass

    def contains(self, key):
        return self.get(key) is not None

    def put(self, key, val=None):
        self._put(key, val, self.root)

    def _put(self, key, val, node):
        pass
