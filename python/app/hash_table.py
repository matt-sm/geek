class HashTable:

    def __init__(self, size=100):
        self.size = size
        self.values = self.size * [None]

    def get(self, x):
        return self.values[self.h(x)]

    def set(self, x, y):
        self.values[self.h(x)] = y

    def h(self, x):
        return hash(x) % self.size
