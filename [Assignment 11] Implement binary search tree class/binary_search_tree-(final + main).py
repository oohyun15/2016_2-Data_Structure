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
                        print()
                        print("--- Successfully inserted. ---")
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
        else:
            return None
                
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
    count = int()
    root = BinarySearchTree(10)
    root.insert(3)
    root.insert(2)
    root.insert(5)
    root.insert(15)
    root.insert(14)
    root.insert(20)
    root.insert(19)
    root.insert(18)
    root.insert(25)    
    print("\n")
    print("  < BinarySearchTree Menu >")
    print(" ┌0. ------  End program ┐")
    print(" │1. -------------  find │")
    print(" │2. ---------  find_min │")
    print(" │3. ---------  find_max │")
    print(" │4. -------  find_floor │")
    print(" │5. --------  find_ceil │")
    print(" │6. -----------  insert │")
    print(" │7. -----------  delete │")
    print(" │8. ---------  find_LCA │")
    print(" │9. ----  shortest_path │")
    print(" │10.---------  diameter │")
    print(" │p.---------  print_BST │")
    print(" │i.--- Inorder_traversal│")
    print(" └m.---------- Open Menu ┘")
    while(1):
        if count == -1:
            break
        print("\n")
        temp = input("▶Select the menu number you want to execute: ")
        while(1):
            if temp == '0': # End program
                count = -1
                break
            
            if temp == '1': # find
                print()
                temp1 = int(input("▷Enter the number you want to find in BST: "))
                print()
                if root.find(temp1) != None:
                    print("--- Number %d exists in BST. ---" %temp1)
                else:
                    print("--- Number %d doesn't exist in BST. ---" %temp1)
                break

            elif temp == '2': # find_min
                print()
                temp2 = root.find_min()
                print("--- Number %d is minimum number in BST. ---" %temp2._element)
                break
    
            elif temp == '3': # find_max
                print()
                temp3 = root.find_max()
                print("--- Number %d is maximum number in BST. ---" %temp3._element)
                break
            
            elif temp == '4': # find_floor
                print()
                temp4 = int(input("▷Enter the number you want to find or floor number in BST: "))
                print()
                if root.find(temp4) != None:
                    print("--- Number %d exists in BST. ---" %temp4)
                else:
                    print("--- Number %d doesn't exist in BST. ---" %temp4)
                    _temp4 = root.find_floor(temp4)
                    if _temp4 == None:
                        print()
                        print("--- Number %d doesn't have floor number. ---" %temp4)
                    else:
                        print()
                        print("--- Number %d is a floor number of %d. ---" %(_temp4._element, temp4))                    
                break
            
            elif temp == '5': # find_ceil
                print()
                temp5 = int(input("▷Enter the number you want to find or ceil number in BST: "))
                print()
                if root.find(temp5) != None:
                    print("--- Number %d exists in BST. ---" %temp5)
                else:
                    print("--- Number %d doesn't exist in BST. ---" %temp5)
                    _temp5 = root.find_ceil(temp5)
                    if _temp5 == None:
                        print()
                        print("--- Number %d doesn't have ceil number. ---" %temp5)
                    else:
                        print()
                        print("--- Number %d is a ceil number of %d. ---" %(_temp5._element, temp5))
                break
            
            elif temp == '6': # insert
                print()
                temp6 = int(input("▷Enter the number you want to insert in BST: "))
                root.insert(temp6)
                #if root.find(temp6) != None:
                     #print("--- Successfully inserted. ---")
                break
            
            elif temp == '7': # delete
                print()
                temp7 = int(input("▷Enter the number you want to delete in BST: "))
                if root.find(temp7) == None:
                    print()
                    print("--- %d number doesn't exist in BST. ---" %temp7)
                else: 
                    _temp7 = root.delete(temp7)
                    print()
                    print("--- Successfully deleted. ---")
                break
            
            elif temp == '8': # find_LCA
                print()
                temp81 = int(input("▷Enter the first number you want to find a LCA in BST: "))
                print()
                temp82 = int(input("▷Enter the second number you want to find a LCA in BST: "))
                temp8 = root.find_LCA(temp81, temp82)
                if temp8 != None:
                    print()
                    print("--- LCA of %d, %d is %d. ---" %(temp81, temp82, temp8._element))
                else:
                    print()
                    print("--- Number %d or %d doesn't exist in BST. ---" %(temp81, temp82))
                break
            
            elif temp == '9': # shortest_path
                print()
                temp91 = int(input("▷Enter the first number you want a shortest path in BST: "))
                if root.find(temp91) == None:
                    print()
                    print("--- Number %d doesn't exist in BST. ---" %temp91)
                    break
                print()
                temp92 = int(input("▷Enter the second number you want a shortest path in BST: "))
                if root.find(temp92) == None:
                    print()
                    print("--- Number %d doesn't exist in BST. ---" %temp92)
                    break
                temp9 = root.shortest_path(temp91, temp92)                
                print()
                print("--- Shortest path of %d, %d is %d. ---" %(temp91, temp92, temp9))
        
                                    
                break

            
            elif temp == '10': # diameter
                print()
                print("--- Diameter in BST is %d. ---" %root.diameter())
                break

            elif temp == 'p': # print_BST
                print()
                print(root)
                break

            elif temp == 'i': # Inorder_traversal
                print()
                print("--- Inorder traversal of BST. ---")
                for i in root.inorder():
                    print(i._element, end =" ")                
                break
            elif temp == 'm': # Open Menu
                print("\n")
                print("  < BinarySearchTree Menu >")
                print(" ┌0. ------  End program ┐")
                print(" │1. -------------  find │")
                print(" │2. ---------  find_min │")
                print(" │3. ---------  find_max │")
                print(" │4. -------  find_floor │")
                print(" │5. --------  find_ceil │")
                print(" │6. -----------  insert │")
                print(" │7. -----------  delete │")
                print(" │8. ---------  find_LCA │")
                print(" │9. ----  shortest_path │")
                print(" │10.---------  diameter │")
                print(" │p.---------  print_BST │")
                print(" │i.--- Inorder_traversal│")
                print(" └m.---------- Open Menu ┘")
                break

            else:
                print()
                print("--- This number doesn't exist. --- ")
                print("\n")
                temp = input("▶Select the menu number you want to execute: ")
               


        

        



            




        
