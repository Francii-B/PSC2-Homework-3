#CLASS TO DEFINE THE NODES OF THE BINARY TREE
class TreeNode:
    #initialization of the tree. No parent, left and right children, by default.
    def __init__(self,key,left=None,right=None,parent=None):
        self.key = key
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    #check if the node has right or left children
    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    #check if the node is a left or a right child
    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    #check if the node is the root of the tree( true if the parent is equal to 'None')
    def isRoot(self):
        return not self.parent

    #check if the node is a leaf of the tree (true if the right and left child a equal to 'None')
    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    #check if the node has any children (true if at least one child is different from 'None')
    def hasAnyChildren(self):
        return (self.rightChild or self.leftChild)

    #check if the node has both children (true if both children are different from 'None')
    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    #Find the minimum value (the leaf on the most left)
    def findMin(self):
      current = self
      while current.leftChild:
          current = current.leftChild
      return current

    #Find the element in the tree which can replace the node
    def findSuccessor(self):
        succ = None
        if self.hasRightChild():
            succ = self.rightChild.findMin()
        else:
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent
                else:
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self
        return succ

    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent

    #replace the node with a new node (change also the parental link to the child)
    def replaceNodeData(self,key,lc,rc):
        self.key = key
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self



#BUILD THE TREE, COMPOSED BY NODES
class BinarySearchTree:

    #initialization: define the root and the size of the tree (no root and size equal to 0)
    def __init__(self):
        self.root = None
        self.size = 0
    
    #insertion of all the elements
    def insertArr(self, array= []):
        for i in array:
            self.put(i)

    #to insert an element into the tree, first we need to check if a root is present or not
    def put(self,key):
        if self.root:
            self._put(key,self.root)
        else:
            self.root = TreeNode(key)
        self.size = self.size + 1

    #compare the new node with current node in the tree
    def _put(self,key,currentNode):
        if key < currentNode.key: #if the new node is smaller, check if the node in the tree already have left child
            if currentNode.hasLeftChild():
                   self._put(key,currentNode.leftChild)
            else:
                   currentNode.leftChild = TreeNode(key,parent=currentNode)
        else:  #if the new node is larger, do the same with the right child
            if currentNode.hasRightChild():
                   self._put(key,currentNode.rightChild)
            else:
                   currentNode.rightChild = TreeNode(key,parent=currentNode)

    #to get an element in the tree, first we must check if a root is present
    def get(self,key):
       if self.root:
           res = self._get(key,self.root)
           if res:
                  return res.key
           else:
                  return None
       else:
           return None

    #compare the element that we want to get with the current one in the tree
    def _get(self,key,currentNode):
       if currentNode.key == key: #if the current el. is equal to the one that we are looking for, return it
           return currentNode
       elif key < currentNode.key and currentNode.hasLeftChild(): #otherwise look among the children
           return self._get(key,currentNode.leftChild)
       elif key > currentNode.key and currentNode.hasRightChild(): #otherwise look among the children
           return self._get(key,currentNode.rightChild)
       else:
           return None

    #check if the element is in the tree
    def __contains__(self,key):
       if self._get(key,self.root):
           return True
       else:
           return False

    #To delete an element off the tree, we must check also if children are present
    def remove(self,currentNode):
         if currentNode.isLeaf(): #leaf
           if currentNode == currentNode.parent.leftChild:
               currentNode.parent.leftChild = None
           else:
               currentNode.parent.rightChild = None
         elif currentNode.hasBothChildren():# both children are present
             succ = currentNode.findSuccessor()
             succ.spliceOut()
             currentNode.key = succ.key

         else: # this node has one child
           if currentNode.hasLeftChild(): #only left child
             if currentNode.isLeftChild():
                 currentNode.leftChild.parent = currentNode.parent
                 currentNode.parent.leftChild = currentNode.leftChild
             elif currentNode.isRightChild():
                 currentNode.leftChild.parent = currentNode.parent
                 currentNode.parent.rightChild = currentNode.leftChild
             else:
                 currentNode.replaceNodeData(currentNode.leftChild.key,
                                    currentNode.leftChild.leftChild,
                                    currentNode.leftChild.rightChild)
           else: #only right child
             if currentNode.isLeftChild():
                 currentNode.rightChild.parent = currentNode.parent
                 currentNode.parent.leftChild = currentNode.rightChild
             elif currentNode.isRightChild():
                 currentNode.rightChild.parent = currentNode.parent
                 currentNode.parent.rightChild = currentNode.rightChild
             else:
                 currentNode.replaceNodeData(currentNode.rightChild.key,
                                    currentNode.rightChild.leftChild,
                                    currentNode.rightChild.rightChild)

    #Module to delete a specific element in the tree. Check if the element is in the tree
    def delete(self,key):
      if self.size > 1:
         nodeToRemove = self._get(key,self.root)
         if nodeToRemove:
             self.remove(nodeToRemove)
             self.size = self.size-1
         else:
             print('This element is not in the tree')
      elif self.size == 1 and self.root.key == key:
         self.root = None
         self.size = self.size - 1
      else:
          print('This element is not in the tree')

    #Find the maximum value (the leaf on the most right)
    def findMax(self):
      current = self.root
      while current.hasRightChild():
          current = current.rightChild
      return current.key

