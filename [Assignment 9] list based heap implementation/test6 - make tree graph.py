class Heap:

    def __init__(self):
        self._data = list()

    def __key(self):
        s = str()
        count = int()
        k = 0
        for i in range(len(self._data)):
            count = count + 1
            if count == 2**k-1:
                print("\n")
            s = s+str(self._data[i][0])
           
          
        return s

    def __parent(self, k):
        return k // 2

    def __left(self, k):
        return 2*k + 1

    def __right(self, k):
        return 2*k + 2

    def __hasLeft(self, k):
        return self.__left(k) < len(self._data)

    def __hasRight(self, k):
        return self.__right(k) < len(self._data)
    
    def __swap(self, i, j):
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def __upheap(self, k):
        parent = self.__parent(k)
        if k> 0 and self._data[k][0] < self._data[parent][0]:
            self.__swap(k, parent)
            self.__upheap(parent)

    def __downheap(self, k):
        if self.__hasLeft(k):
            left = self.__left(k)
            temp = left
            if self.__hasRight(k):
                right = self.__right(k)
                if self._data[right][0] < self._data[left][0]:
                    temp = right
            if self._data[temp][0] < self._data[k][0]:
                 self.__swap(k, temp)
                 self.__downheap(temp)
        
    
    def insert(self,key, value):
        self._data.append((key, value))
        self.__upheap(len(self._data)-1)
       # return self._data

    def removeMin(self):
        if self._data == []:
            raise Empty('List is empty.')
        self.__swap(0, len(self._data)-1)
        temp = self._data.pop()
        self.__downheap(0)
        return temp

if __name__ == "__main__":
    h = Heap()
    h.insert(0, None)
    h.insert(1, None)
    h.insert(3, None)
    h.insert(1, None)
    h.insert(4, None)
    h.insert(9, None)
    h.insert(4, None)
    h.insert(2, None)
    h.insert(8, None)
    h.insert(6, None)
    
