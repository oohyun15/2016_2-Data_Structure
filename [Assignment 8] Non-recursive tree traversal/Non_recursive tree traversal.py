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
class BinaryTree:
    def __init__(self, element, parent=None, left=None, right=None):
        __slots__ = '_element', '_parent', '_left', '_right'
        
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
        newTree = BinaryTree(newElement, self)
        if self._left == None:
            self._left = newTree
        else:
            newTree._left = self._left
            self._left._parent = newTree
            self._left = newTree
        return newTree
            
    def addRight(self, newElement):
        newTree = BinaryTree(newElement, self)
        if self._right == None:
            self._right = newTree
        else:
            newTree._right = self._right
            self._right._parent = newTree
            self._right = newTree
        return newTree
            
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

    def preorder_nonrecursive(self):
        stack = Stack()
        stack.push(self)
        while not stack.isEmpty():
            node = stack.pop()
            yield node
            if node._right != None:
                stack.push(node._right)
            if node._left != None:
                stack.push(node._left)

    def inorder_nonrecursive(self):
        stack = Stack()
        stack.push(self)
        while not stack.isEmpty():
           # print("\n\tsize",stack.size())
            node = stack.pop()
            if node._right != None:
                stack.push(node._right)
                if node._left == None: # X O
                    yield node   
            if node._left != None:
                stack.push(node)
                stack.push(node._left)
            if node.isExternal(): # X X
                yield node
                if stack.isEmpty():
                        break
                while not stack.top().isRoot() and (stack.top().getParent().getLeft() == None or stack.top().getParent().getRight() ==None):
                    temp = stack.pop()
                    yield temp
                if stack.top().isInternal(): 
                    nodeParent = stack.pop()
                    yield nodeParent
                    

    def postorder_nonrecursive(self):
        stack = Stack()
        stack.push(self)
        while not stack.isEmpty():
            node = stack.pop()
            if node.isInternal():
                stack.push(node)
            if node._right != None:
                stack.push(node._right)
            if node._left != None:
                stack.push(node._left)
            if node.isExternal():
                yield node
                while stack.top() == node.getParent():
                    temp = stack.pop()
                    yield temp
                    node = node.getParent()
                    if stack.isEmpty():
                        break
              
        
    
        
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
    root = BinaryTree('1')
    root.addLeft('2')
    root.addRight('3')
    root.getLeft().addLeft('4')
    root.getLeft().addRight('5')
    root.getRight().addLeft('6')
    root.getRight().addRight('7')
    root.getRight().getLeft().addRight('8')
#    root.getRight().getRight().addRight('10')
#    root.getRight().getLeft().addLeft('8')
#    root.getRight().getLeft().getLeft().addLeft('11')
#    root.getRight().getLeft().getLeft().addRight('12')
#    root.getRight().getLeft().getRight().addLeft('13')
#    root.getRight().getLeft().getRight().addRight('14')
#    root.getRight().getLeft().getRight().getLeft().addRight('15')

#    print(root)
#    print("\n")
#    print(root.getLeft())
#    print("\n")
#    print(root.getLeft().getSibling())
#    print("\n")
#    print(root.getLeft().getLeft())
#    print("\n")
#    print(root.getLeft().getRight())
#    print("\n")
#    print(root.getRight().getLeft())
#    print("\n")
#    print(root.getRight().getRight())
    
#    t = root.getLeft()
#    print("Depth of {}: {}".format(t.getElement(), t.depth()))
#    print("Height of {}: {}".format(t.getElement(), t.height()))
#    print("{} is".format(t.getElement()), "internal." if t.isInternal() else "external.")
#    print("{} is".format(t.getElement()), "a root." if t.isRoot() else "not a root.")

#    print(t.getSibling().getElement())

    print("\nInorder Traversal")
    for p in root.inorder():
        print(p.getElement(), end=" ")
    print("\n")
    
    print("\nInorder_nonrecursive Traversal")
    for p in root.inorder_nonrecursive():
        print(p.getElement(), end=" ")
    print("\n")

    print("\nPreorder Traversal")
    for p in root.preorder():
        print(p.getElement(), end=" ")
    print("\n")
    
    print("\nPreorder_nonrecursive Traversal")
    for p in root.preorder_nonrecursive():
        print(p.getElement(), end=" ")
    print("\n")

    print("\nPostorder Traversal")
    for p in root.postorder():
        print(p.getElement(), end=" ")
    print("\n")
    
    print("\nPostorder_nonrecursive Traversal")
    for p in root.postorder_nonrecursive():
        print(p.getElement(), end=" ")
    print("\n")

    
    print("\nLevelorder Traversal")
    for p in root.levelorder():
        print(p.getElement(), end=" ")
        last = p
    print("\n")
    
    print("The last is ", last.getElement())
