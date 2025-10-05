'''Binary search tree
Special type of binary tree ( atmost 2 children)
left child  => less than parent
right child => grater thatn parent

Applications => sorting, searching, database indexing, 

inorder traversal will give you a sorted array

| Operation | Average Case | Worst Case (Skewed Tree) |
| --------- | ------------ | ------------------------ |
| Search    | O(log n)     | O(n)                     |
| Insertion | O(log n)     | O(n)                     |
| Deletion  | O(log n)     | O(n)                     |
| Traversal | O(n)         | O(n)                     |


Tree Traversal =>

    inorder => left, root, right
    preorder => root, left, right
    postorder => left, right, root



check week 16 in the tracker sheet
https://docs.google.com/spreadsheets/d/1YE98QKlEqcQOC9lCIHANE2yZorHf4IttgW-TGChl_z8/edit?gid=1938016385#gid=1938016385


'''

from collections import deque

#definition NOde
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

#BST
class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert(self.root, data)

    def _insert(self, root, data):
        if root is None:
            return Node(data)
        
        if data < root.data:
            root.left = self._insert(root.left, data)
        if data > root.data:
            root.right = self._insert(root.right, data)

        return root # we need return here because someone is wating for a return value. ex, self.root =  line is expecting a return value.
    
    def level_order(self):
        if self.root is None:
            return
        queue = deque()
        queue.append(self.root)
        
        while queue:
            
            for _ in range(len(queue)):
            
                current = queue.popleft()
                print(current.data, end=" ")
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            print()

    def search(self, data):
        if self.root is None:
            return False
        
        current = self.root
        while current:
            if data==current.data: return True
            elif data < current.data: current = current.left
            else: current = current.right

        return False
    
    #traversal

    def inorder(self):
        '''It  will return a sorted arary'''
        print("Inorder Travesal: ", end=" ")
        def _inorder(root):
            if root is None: return
            _inorder(root.left)
            print(root.data, end=" ")
            _inorder(root.right)
        
        _inorder(self.root)
        print()

    def preorder(self):
        '''root, left, right'''
        print("Preorder: ", end=" ")
        def _preorder(root):
            if root is None: return
            print(root.data, end= " ")
            _preorder(root.left)
            _preorder(root.right)

        _preorder(self.root)
        print()

    
    def delete(self, data):
        '''
        for deleting value, we have 3 conditions

        first search for the node

        1. node is a leaf node  => just delete the node
        2. node has only one child => swap the nodes and delete the leaf node
        3. node has 2 child => find the inorder successor (min value/the deepest left child from the right sub tree)
                               replace this node with the root node(the deletion node)
                               now, the node to be deleted in at leaf node, delete it now 
        
        '''
        self.root = self._delete(self.root, data)

    def _delete(self, root, data):

        if root is None:
            return None
        
        #search for the node
        if data < root.data:
            root.left = self._delete(root.left, data)
        elif data > root.data:
            root.right = self._delete(root.right, data)

        else:
            #found the data, now check the conditions


            #case 1 => no leaf node
            if root.left is None and root.right is None:
                return None
            
            #case 2 => one leaf node
            if root.left is None: #means only right child is there. so return the right child. it will be stored in the root
                return root.right
            elif root.right is None:
                return root.left
            
            #case 3 => find inorder successor
            min_val = self._inorder_successor(root.right)
            #replace it with the node to be delted
            root.data = min_val.data
            #delete the actual min node., that should be a leaf node
            root.right = self._delete(root.right, min_val)

        return root


    def _inorder_successor(self, root):
        
        while root.left:
            root = root.left
        
        return root
        

        



        


    

    
bst = BST()
bst.insert(10)
bst.insert(15)
bst.insert(5)
bst.insert(1)
bst.insert(6)
bst.inorder()

# bst.delete(15)



# bst.level_order()

# print(bst.search(2))
bst.inorder()
# bst.preorder()
