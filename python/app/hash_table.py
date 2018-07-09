class HashTable:

    def __init__(self, size=100):
        self.size = size
        self.values = self.size * [None]

    def get(self, x):
        if not x:
            raise ValueError('Invalid key')

        i = self.h(x)
        result = None

        if self.values[i]:
            pair = [p[1] for p in self.values[i] if p[0] == x]
            if pair:
                result = pair[0]

        return result

    def set(self, x, y):
        """Uses separate chaining for collsions
        """
        if not x:
            raise ValueError('Invalid key')

        i = self.h(x)

        if not self.values[i]:
            self.values[i] = []

        self.values[i].append([x, y])

    def h(self, x):
        return hash(x) % self.size
