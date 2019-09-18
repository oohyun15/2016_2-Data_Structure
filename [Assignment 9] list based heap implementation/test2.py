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


"""Node and reference implementation of a binary tree"""
class Heap:
    def __init__(self, key, element, parent=None, left=None, right=None):
        __slots__ = '_value', '_element', '_parent', '_left', '_right'

        self._key = key
        self._element = element
        self._parent = parent
        self._left = left
        self._right = right

    
    
    def getParent(self):
        return self._parent
        
    def getLeft(self):
        return self._left
        
    def getRight(self):
        return self._right
        
    def getSibling(self):
        if self.isRoot():
            return None
        elif self.getParent().getLeft() == self:
            return self.getParent().getRight()
        elif self.getParent().getRight() == self:
            return self.getParent.getLeft()
        else:
            raise ValueError("Strange Node")
        
    def _setParent(self, container):
        self._parent = container
    
    def _setLeft(self, lChild):
        self._left = lChild
        
    def _setRight(self, rChild):
        self._right = rChild
        
    def addLeft(self, newElement):
        newTree = Heap(newElement, self)
        if self._left == None:
            self._left = newTree
        else:
            newTree._left = self._left
            self._left._parent = newTree
            self._left = newTree
        return newTree
            
    def addRight(self, newElement):
        newTree = Heap(newElement, self)
        if self._right == None:
            self._right = newTree
        else:
            newTree._right = self._right
            self._right._parent = newTree
            self._right = newTree
        return newTree

    def getKey(self):
        return self._key

    def setKey(self, key):
        self._key = key
            
    def getElement(self):
        return self._element
        
    def setElement(self, element):
        self._element = element
        
    def __str__(self):
        return "[ "+str(self._element)+" "+str(self._left)+" "+str(self._right)+" ]"#preorder traversal

    def inorder(self):
        if self._left != None:
            for other in self._left.inorder():
                yield other
        yield self
        if self._right != None:
            for other in self._right.inorder():
                yield other
    
    def preorder(self):
        yield self
        if self._left != None:
            for other in self._left.preorder():
                yield other
        if self._right != None:
            for other in self._right.preorder():
                yield other

    def postorder(self):
        if self._left != None:
            for other in self._left.postorder():
                yield other
        if self._right != None:
            for other in self._right.postorder():
                yield other
        yield self

    def levelorder(self):
        queue = []
        queue.append(self)
        while len(queue) != 0:
            p = queue.pop(0)
            if p._left != None:
                queue.append(p._left)
            if p._right != None:
                queue.append(p._right)
            yield p

    def children(self):
        if self._left:
            yield self._left
        if self._right:
            yield self._right
            
    def depth(self):
        if self._parent == None:
            return 0
        else:
            return 1+self._parent.depth()
            
    def isInternal(self):
        return self._left or self._right
        
    def isExternal(self):
        return not self.isInternal()
        
    def isRoot(self):
        return self._parent == None
        
    def height(self):
        if self.isExternal():
            return 0
        else:
            return 1 + max(c.height() for c in self.children())
    
    def delete(self):
        if self._parent:
            if self._parent._left == self:
                self._parent._left = None
            elif self._parent._right == self:
                self._parent._right = None
            else:
                raise ValueError("Strange node cannot be deleted")
        
        self._parent = None
        for c in self.children():
            c.delete()
        
        self._left = self._right = self._element = None
        del self
        self = None
            
if __name__ == "__main__":
    root = Heap('1')
    root.addLeft('2')
    root.addRight('3')
    root.getLeft().addLeft('4')
    root.getLeft().addRight('5')
    root.getRight().addLeft('6')
    root.getRight().addRight('7')
    root.getRight().getLeft().addRight('8')

    print(root)
    print("\n")
    print(root.getLeft())
    print("\n")
    print(root.getLeft().getSibling())
    print("\n")
    print(root.getLeft().getLeft())
    print("\n")
    print(root.getLeft().getRight())
    print("\n")
    print(root.getRight().getLeft())
    print("\n")
    print(root.getRight().getRight())
    
    t = root.getLeft()
    print("Depth of {}: {}".format(t.getElement(), t.depth()))
    print("Height of {}: {}".format(t.getElement(), t.height()))
    print("{} is".format(t.getElement()), "internal." if t.isInternal() else "external.")
    print("{} is".format(t.getElement()), "a root." if t.isRoot() else "not a root.")

