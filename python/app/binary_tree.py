class BNode:

    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

    def __str__(self):
        ''' Preorder traversal
        '''
        s = '{}{}'.format(str(self.val), ' ')
        if self.left is not None:
            s += str(self.left)

        if self.right is not None:
            s += str(self.right)

        return s

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
