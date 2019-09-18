class PriorityQueueBase:

    class _Item:

        __slots__ = '_key', '_value'

        def __init__(self,k, v):
            self._key = k
            self._value = v

        def __lt__(self, other):
            return self._key < other._key # compare items based on their keys

        def is_empty(self):
            return len(self) == 0

        def getKey(self):
            return self._key

        def getValue(self):
            return self._value


class HeapPriorityQueue(PriorityQueueBase):

    def __is_empty__(self):
        return self._data == [] 
    def __parent__(self, j):
        return (j-1) // 2

    def __left__(self, j):
        return 2*j + 1

    def __right__(self, j):
        return 2*2 + 2

    def __has_left__(self, j):
        return self.__left__(j) < len(self._data)

    def __has_right__(self, j):
        return self.__right__(j) < len(self._data)

    def __swap__(self, i, j):
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def __upheap__(self, j):
        parent = self.__parent__(j)
        if j > 0 and self._data[j] < self._data[parent]:
            self.__swap__(j, parent)
            self.__upheap__(parent) #recur at position of parent
        raise NotImplementedError('test')

    def __downheap__(self, j):
        if self.__has_left__(j):
            left = self.__left__(j)
            small_child = left
            if self.__has_right__(j):
                right = self.__right__(j)
                if self._data[right] < self._data[left]:
                    small_child = right
            if self._data[small_child] < self._data[j]:
                self.__swap__(j, small_child)
                self.__downheap__(small_child) # recur at position of small child

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def add(self, key, value):
        self._data.append(self._Item(key, value))
        self.__upheap__(len(self._data)-1) # upheap newly added position


    def remove_min(self):
        if self.is_empty():
            raise Empty('Priority queue is empty.')
        self._swap(0, len(self._data)-1) #put minimum item at the end
        item = self._data.pop() #and remove it from the list
        self.__downheap__(0)   #then fix new root
        return (item._key, item._value)



if __name__ == "__main__":

    HL = HeapPriorityQueue()
    HL.add(1,1)
    HL.add(2,2)
    HL.add(4,4)
    
    
    

    
