"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
#NOTES:
# the point of binary search trees is that you don't have to search the entire tree for the target. You can quickly eliminate halves of the tree that you don't need to look in based on the target's value compared to the value of the other nodes. Whereas in an array, you have to compare the value to every node in the array until you find the target, which could be very time consuming.
# unlinke the linked list, we only have access to the root here. we don't have a head and a tail to go from.

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        #check if value is < current node's value, if yes -> go left
        if value < self.value:
            #check if the current node has a left child? if NO left child, then wrap value in BTSNode and set the new node here, it found its place.
            if self.left is None:
                self.left = BSTNode(value)
            #otherwise, there is a left child, so we can call the left child's insert method to insert the value here
            else:
                self.left.insert(value)
        #otherwise, the value is >= the current node's value, and we need to go right
        else:
            #does the current node have a right child? if NO right child, wrap the value in BTSNode and set the node here.
            if self.right is None:
                self.right = BSTNode(value)
            #otherwise, there is a child, so call the right child's insert method to insert the value here
            else:
                self.right.insert(value)
    
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        #first, determine if the target is equal to the current node's value
        #if yes, return True, we are finished
        if target == self.value:
            return True
        #check if the target value is < the current node's value
        #if yes, determine if the left child exists
        if target < self.value:
            if not self.left:
                #if no left child, return False
                return False
            else:
                #otherwise, the target is on the left child
                return self.left.contains(target)
        #otherwise, the value is > the current node, so we can determine if there is a right child
        else:
            #check if there is no child on the right
            if not self.right:
                return False
            else:
                #the right child contains the target
                return self.right.contains(target)


    # Return the maximum value found in the tree
    # remember that larger value numbers go to the right
    def get_max(self):
        #if the tree is empty, return None
        if not self:
            return None
        #while there is a right child, move to the right
        #if we keep moving to the right, we will keep getting the larger value
        while self.right:
            self = self.right
        #once there is no child to return, return the value because it will be the larget, the max
        return self.value


    #Call the function `fn` on the value of each node
    #this method does not return anything
    def for_each(self, fn):
        #call fn on the root node's value
        fn(self.value)
        #check if there is a left child
        if self.left:
            #call for each fn on the left child
            self.left.for_each(fn)
        #check if there is a right child
        if self.right:
            #call for each fn on the right child
            self.right.for_each(fn)
        #otherwise, there is no right child


    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    # def in_order_print(self):
    #     pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    # def bft_print(self):
    #     pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    # def dft_print(self):
    #     pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    # def pre_order_dft(self):
    #     pass

    # Print Post-order recursive DFT
    # def post_order_dft(self):
    #     pass

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

# bst.bft_print()
# bst.dft_print()

# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
# print("in order")
# bst.in_order_dft()
# print("post order")
# bst.post_order_dft()  
