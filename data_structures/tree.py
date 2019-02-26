class Tree:

    class Node:

        def __init__(self, item):
            self.data = item
            self.children = []

    def __init__(self):
        self.root = None

    def find_node(self, item):

        def find(root, item):
            if root.data == item:
                return root
            else:
                for child in root.children:
                    return find(child, item)

        if self.root == None:
            return None
        else:
            return find(self.root, item)

    def print(self):

        def p(node, prefix=' '):
            print(prefix, node.data)
            for child in node.children:
                p(child, prefix * 2)

        p(self.root)

    def add_node(self, item, parent=None):
        if not parent:
            self.root = Tree.Node(item)
        else:
            node = self.find_node(parent)
            node.children.append(Tree.Node(item))

tree = Tree()
tree.add_node(11)
tree.add_node(22, 11)
tree.add_node(33, 22)
tree.add_node(44, 22)
tree.add_node(55, 33)

print(tree.find_node(66))
tree.print()