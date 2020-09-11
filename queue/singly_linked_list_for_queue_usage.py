class Node:
    def __init__(self, value):
        #the value that the node is holding
        self.value = value
        #reference to the next node in the linked list
        self.next = None
    
    #method to get the value of the node
    def get_value(self):
        return self.value
    
    #method to get the node's next_node
    def get_next(self):
        return self.next

    #method to update the node's next_node to the input node 
    def set_next(self, new_next):
        self.next = new_next

# ll = Node(1)
# ll.set_next(Node(2))
# ll.next.set_next(Node(3))
# ll.next.next.set_next(Node(4))
# ll.next.next.next.set_next(Node(5))

#this way of doing it is tedious.
# so lets do it a better way!
 
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        # 1. create the Node from the value
        new_node = Node(value)
        #What to do if tail is None?
        #What to do if the list is empty and there is no head?
        #Lets check for both possibilities.
        if self.head is None and self.tail is None:
            # in a one-element linked list, what should head and tail be pointing to?
            # lets have both head and tail refer to the single node
            self.head = new_node
            # set the new node to be the tail
            self.tail = new_node
            # otherwise, the list has at least one node, so we need to add the new node to the tail
        else:
            # These steps assume that the tail is already referring to a Node
            # 2. set the old tail's next to refer to the new Node
            self.tail.set_next(new_node)
            # 3. reassign self.tail to refer to the new Node we just added
            self.tail = new_node

    def remove_tail(self):
        #check if the linked list is empty
        if self.head is None and self.tail is None:
            return None
        #check if the linked list has only one node
        if self.head == self.tail:
            #store the node we're going to remove's value
            val = self.head.get_value()
            self.head = None
            self.tail = None
            return val
        # otherwise, the linked list has more than one Node
        else:
            # store the last Node's value in another variable so we can return it
            val = self.tail.get_value()
            # we need to set self.tail to the second-to-last Node
            # to do this, we need to traverse the whole linked list from the beginning
            # starting from the head, we'll traverse down to the second-to-last Node
            # init another reference to keep track of where we are in the linked list we're iterating
            current = self.head
            # keep iterating until the node after `current` is the tail
            while current.get_next() is not self.tail:
                # keep iterating
                current = current.get_next()
            #at this point, `current` is the node right before the tail

            # set the tail to be None
            self.tail = None
            # move self.tail to the Node right before
            self.tail = current
            # set the new tail's `next_node` to None
            self.tail.set_next(None)
            return val

    def remove_head(self):
        # check if the linked list is empty
        if self.head is None and self.tail is None:
            return None
        # check if there is only one linked list node (a single element)
        if self.head == self.tail:
            val = self.head.get_value()
            # delete the list's head reference
            self.head = None
            # also make sure the tail reference doesn't refer to anything
            self.tail = None
            # return the value
            return val
        # otherwise we have more than one element in our list
        else:
            # store the old head's value that we need to return
            val = self.head.get_value()
            # set the `self.head` to the old head's `next_node`
            self.head = self.head.get_next()
            #return the old_head's value
            return val

    def contains(self, value):
        if not self.head:
            return False
        # get a reference to the node we're currently at; update this as we traverse the list
        current = self.head
        # check to see if we're at a valid node 
        while current:
            # return True if the current value we're looking at matches our target value
            if current.get_value() == value:
                return True
            # update our current node to the current node's next node
            current = current.get_next()
        # if we've gotten here, then the target node isn't in our list
        return False

    def get_max(self):
        if not self.head:
            return None
        #reference to the largest value we've seen so far
        max_value = self.head.get_value()
        #reference to our current node as we traverse the list
        current = self.head.get_next()
        #check to see if we are still at a valid list node
        while current:
            #check to see if the current value is greater than the max_value
            if current.get_value() > max_value:
                #if so, update our max_value variable
                max_value = current.get_value()
            #update the current node to the next node in the list
            current = current.get_next()
        return max_value