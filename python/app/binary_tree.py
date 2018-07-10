class BNode:

    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, node):
        if node.val < self.val:
            if self.left is None:
                self.left = node
            else:
                self.left.insert(node)

        if node.val > self.val:
            if self.right is None:
                self.right = node
            else:
                self.right.insert(node)
