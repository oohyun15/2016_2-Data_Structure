import ctypes
import matplotlib.pyplot as plt
import time

class DynamicArray_doubling:
    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        if not 0 <= k < self._n:
            raise IndexError('invalid index')
        return self._A[k]

    def append(self, obj):
        if self._n == self._capacity:
            self._resize(2*self._capacity) # so double capacity
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c):
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c

    def _make_array(self, c):
        return (c*ctypes.py_object)()

class DynamicArray_increamental:
    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        if not 0 <= k < self._n:
            raise IndexError('invalid index')
        return self._A[k]

    def append(self, obj):
        if self._n == self._capacity:
            self._resize(self._capacity+50) # so increament in 50 capacity
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c):
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c

    def _make_array(self, c):
        return (c*ctypes.py_object)()

if __name__ == '__main__':
    
    arr1 = DynamicArray_doubling()
    S = []
    bgn1 = time.time()
    for i in range(2**14):
        arr1.append(i)
        end1 = time.time()
        S.append(end1-bgn1)
        
    arr2 = DynamicArray_increamental()
    SS = []
    bgn2 = time.time()
    for i in range(2**14):
        arr2.append(i)
        end2 = time.time()
        SS.append(end2-bgn2)

    SSS = []
    for i in range(2**14):
        SSS.append(SS[i]-S[i])

    #fig = plt.figure()
    #ax = fig.add_subplot(111)
    #ax.set_xscale("log")
    #ax.set_yscale("liner")
    #ax.set_aspect(1)
    plt.title("Experimental amortized analysis of dynamic array")
    dou, = plt.plot([x for x in range(2**14)],S)
    inc, = plt.plot([x for x in range(2**14)],SS)
    sub, = plt.plot([x for x in range(2**14)],SSS)
    plt.legend([dou, inc, sub],['Doubling','Increamental', 'Subsractive'], loc=3)
    plt.xlabel("Current number of elements")
    plt.ylabel("Time(sec)")
    plt.axis([0,2**14,0,None])
    plt.show()

