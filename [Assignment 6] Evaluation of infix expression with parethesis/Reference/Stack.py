class Stack:
    """ General stack implementation using a Python list at the end. """
    def __init__(self):
        self._items = []

    def __str__(self):
        return str(self._items)

    def __repr__(self):
        return str(self._items)

    def isEmpty(self):
        return self._items == []

    def size(self):
        return len(self._items)

    def push(self, item):
        self._items.append(item)

    def pop(self):
        try:
            e = self._items.pop()
        except IndexError:
            print("Empty stack exception")
            return

        return e

    def top(self):
        return self._items[-1]

if __name__ == "__main__":
    from time import time
    maxN = 10000
    S = Stack()
    start = time()
    for i in range(maxN):
#               print("Pushing {0:2d}".format(i))
        S.push(i)
    end = time()
    print("Pusing {0} items into S requires {1}".format(maxN, (end-start)*1000000))

    start = time()
    while not S.isEmpty():
        e = S.pop()
#               print("Popping {0:2d}".format(e))
    end = time()
    print("Popping {0} items from S requires {1}".format(maxN, (end-start)*1000000))
