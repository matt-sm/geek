class Node:

    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        n = self
        str = ''
        while n is not None:
            str += '{}{}'.format(n.val, '' if n.next is None else ' ')
            n = n.next

        return str

    def delete(self, node):
        n = self
        while n.next is not node:
            n = n.next

        n.next = node.next

    def kth_from_last(self, count):
        n = self
        ref = self

        i = 1
        while i < count:
            ref = ref.next
            i += 1

        while ref.next is not None:
            n = n.next
            ref = ref.next

        return n
