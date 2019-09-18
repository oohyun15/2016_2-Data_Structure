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
    
    def _delete(self):
        if self._parent:
            if self._parent._left == self:
                self._parent._left = None
            elif self._parent._right == self:
                self._parent._right = None
            else:
                raise ValueError("Strange node cannot be deleted")
        






"""Node and reference implementation of a binary search tree."""
class BinarySearchTree(BinaryTree):
    def _swap_element(self, i, j):
        i._element, j._element = j._element, i._element
 
    def __init__(self, element, parent=None, left=None, right=None):
        super().__init__(element)
        
    def find(self, element):
        '''Find and return a node contains element. If not exist return None'''
        if element == self._element:
            return self
        elif element < self._element and self._left != None:
            return self._left.find(element)
        elif element > self._element and self._right != None:
            return self._right.find(element)
      #  print(str(element)+" doesn't exist this BinarySearchTree")
        return None

    def find_min(self):
        '''Find and return a node contains the minimum element'''
        if self._left == None:
            return self
        temp = self._left
        while(temp._left != None):
            temp = temp._left
        return temp
        
    def find_max(self):
        '''Find and return a node contains the maximum element'''
        if self._right == None:
            return self
        temp = self._right
        while(temp._right != None):
            temp = temp._right
        return temp
         

    def find_floor(self, element):
        '''Find and return a node contains element. If not exist return a node the maximum among nodes less than the element'''
        temp1=self.find(element)
        if temp1 == None:
            if element <self.find_min()._element:
               # print("There is no node in element that is less than %d." %element)
                return None
            else:
                self.insert(element)
                temp=self.find(element)
                for i in self.inorder():
                    if temp == i:
                        break
                    temp1 = i
                self.delete(element)
        return temp1

    def find_ceil(self, element):
        '''Find and return a node contains element. If not exist return a node the minimum among nodes greater than the element'''
        temp1=self.find(element)
        if temp1 == None:
            if element >self.find_max()._element:
               # print("There is no node in element that is more than %d." %element)
                return None
            else:
                self.insert(element)
                temp=self.find(element)
                count = int()
                for i in self.inorder():
                    temp1 = i
                    if count == 1:
                        break
                    if temp == i:
                        count = 1
                self.delete(element)
        return temp1

    def insert(self, element):
        '''Insert a node of element while preserving BST property after the insertion'''
        
        if element < self._element:
            if self._left == None:
                temp = BinarySearchTree(element, self)
                self._left = temp
                temp._parent = self
            else:
                self._left.insert(element)
        elif element > self._element:
            if self._right == None:
                temp = BinarySearchTree(element, self)
                self._right = temp
                temp._parent = self
            else:
                self._right.insert(element)
        else:
            while(1):
                ipt = input("Same element exists. DO YOU WANT INSERT THIS ELEMENT IN NEW NODE? (Y/N): ")
                if  'Y' == ipt:
                    temp = BinarySearchTree(element, self)
                    if self._left == None:
                        self._left = temp
                        temp._parent = self
                    else:
                        self._left.insert(element)
                    break
                elif 'N' == ipt:
                    break
    
    def delete(self, element):
        '''Delete a node of element while preserving BST property after the removal'''
        temp = self.find(element)
        if temp != None:
            #print(temp.isExternal())
            if temp.isExternal():
                temp._delete()
            else:
                for i in root.inorder():
                    if temp == i:
                        break
                    temp1 = i
              #  print(temp1)
                self._swap_element(temp, temp1)
                temp1._delete()
              #  print(temp)
                
    def find_LCA(self, element1, element2):
        '''Find and return the lowest common ancestor(LCA) of element1 and element2.
        If either of element1 or element2 does not exist, return None'''
        temp1 = self.find(element1)
        temp2 = self.find(element2)
        if temp1 == None or temp2 == None:
            return None
        else:
            if temp1 == temp2:
                return temp1
            else:
                if temp1.depth() > temp2.depth():
                    while(temp1.depth() != temp2.depth()):
                        temp1 = temp1._parent
                elif temp1.depth() < temp2.depth():
                    while(temp1.depth() != temp2.depth()):
                        temp2 = temp2._parent
                if temp1 == temp2:
                    return temp1 # or temp2
                else:
                    while (temp1._parent != temp2._parent):
                        temp1 = temp1._parent
                        temp2 = temp2._parent
                    return temp1._parent # or temp2._parent

        
    def shortest_path(self, element1, element2):
        '''Find and return the shortest path (list of nodes) from element1 to element2.
        If either of element1 or element2 does not exist, return None'''
        temp1 = self.find(element1)
        temp2 = self.find(element2)
        if temp1 == None or temp2 == None:
            return None
        else:
            temp = temp1.depth() + temp2.depth() - 2*root.find_LCA(element1, element2).depth()
            return temp
        
    def diameter(self):
        '''Compute and return the diameter of a tree rooted at self'''
        for i in self.levelorder():
            temp = i # 루트로 부터 가장 먼 노드 중 하나
        #print(temp._element)
        temp1 = int()
        for i in self.levelorder():
            if temp1 < self.shortest_path(temp._element, i._element):
                temp1 = self.shortest_path(temp._element, i._element)
                #print(i._element)
        return temp1
            
    
if __name__ == "__main__":
    root = BinarySearchTree(6)
    root.insert(4)
    root.insert(8)
    root.insert(2)
    root.insert(5)
    root.insert(10)
    root.insert(7)
    root.insert(1)
    root.insert(3)

    print("Inorder traversal of BST.")
    for i in root.inorder():
        print(i._element, end =" ")
    print("\n")
    temp = int(input("Enter what you want to find number: "))
    print()
    if root.find(temp) != None:
        print("There is a element %d in BST" %temp)
    else:
        print("There is not element %d in BST" %temp)
        print()
        temp1 = root.find_floor(temp)
        temp2 = root.find_ceil(temp)
        if  temp1!= None:
            print("There is a floor element %d in BST" %temp1._element)
        if temp2 != None:
            print("There is a ceil element %d in BST" %temp2._element)
    print("\n")
    print("find_max element is "+str(root.find_max()._element))
    print("find_min element is "+str(root.find_min()._element))
    print("\n")

    temp3 = int(input("Enter what you want to insert number: "))
    print()
    root.insert(temp3)
    for i in root.inorder():
        print(i._element, end =" ")
    print("\n")
    temp4 = int(input("Enter what you want to delete number: "))
    print()
    root.delete(temp4)
    for i in root.inorder():
        print(i._element, end =" ")
    print("\n")
    temp6 = root.find_LCA(3, 10)
    print("LCA of 3, 10 is %d element." %(temp6._element))
    print("\n")
    temp7 = root.shortest_path(2, 10)
    print("Shortest path of 2,10 is %d."%temp7)
    print("\n")
    temp8 = root.diameter()
    print("Diameter of this BST is %d." %temp8)
    
    
