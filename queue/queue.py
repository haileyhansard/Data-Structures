"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""

# Queue: FIRST IN FIRST OUT, like waiting in a pharmacy line, first one in line gets to receive rx and get out of store first
# enqueue - adds an item to end of queue (tail)
# dequeue - removes the front item (head or index[0])

# ARRAY VERSION

# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []
    
#     def __len__(self):
#         return self.size

#     def enqueue(self, value):
#         #add value to end of array
#         self.storage.append(value)
#         #update size
#         self.size += 1

#     def dequeue(self):
#         #check if array is not empty
#         if self.size != 0:
#             #update size
#             self.size -= 1
#             #remove the oldest added value --> index 0
#             return self.storage.pop(0)

# 4 tests passing

# LINKED LISTS VERSION
from singly_linked_list_for_queue_usage import LinkedList

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def enqueue(self, value):
        #add value to the tail
        self.storage.add_to_tail(value)
        #update size
        self.size += 1

    def dequeue(self):
        #check if linked list is not empty
        if self.size != 0:
            #update size
            self.size -= 1
            #remove the oldest added value --> head
            return self.storage.remove_head()

# 4 tests passing


