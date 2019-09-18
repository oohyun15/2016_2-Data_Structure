class Heap(self):

    class _Queue:
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

        def enqueue(self, item):
            self._items.append(item)

        def dequeue(self):
            try:
                e = self._items[0]
            except IndexError:
                print("Empty queue exception")
                return
            del self._items[0]
            return e

        

        


    def __init__(self):
        
    
    def insert(self):

    def removeMin(self):
        
