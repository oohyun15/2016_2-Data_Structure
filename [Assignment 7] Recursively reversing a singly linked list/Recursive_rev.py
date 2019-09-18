class LinkedList:

    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next
        def getNext(self):
            return self._next
        def setNext(self, next):
            self._next = next
        def getElement(self):
            return self._element

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, e):
        self._head = self._Node(e, self._head)
        self._size += 1

    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._head._element

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer

    def recursive_rev(self, head):
        if head == None or head.getNext() == None:
            return head
        tail = head.getNext()
        head.setNext(None)
        newhead = self.recursive_rev(tail)
        print("head",head.getElement(),"tail",tail.getElement(),"newhead",newhead.getElement())
        tail.setNext(head)
        return newhead
        
        
if __name__ == '__main__':
    linkedList = LinkedList()

    for i in range(10):
        linkedList.push(i)
    
    temp = linkedList._head
    for i in range(10):
        print(temp._element, end= ' ')
        temp = temp._next
    print()
    temp = linkedList.recursive_rev(linkedList._head)
    for i in range(10):
        print(temp._element, end= ' ')
        temp = temp._next
        
    



