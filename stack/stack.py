"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

#Stack: LAST IN FIRST OUT (like a stack of plates)
# Push: we add (append) an item to the top of the stack (tail/ most recently added item)
# Pop: we remove the item most recently added (tail)
# a Stack is a recursive data structure. It is either empty, or, it consists of a top and the rest which is a stack.
# ex of using a Stack in real world: undo mechanism in text editors. all text changes are kept in a stack, 

# USING ARRAYS:
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return self.size

#     def push(self, value):
#         self.size += 1
#         self.storage.append(value)

#     def pop(self):
#         if self.size == 0:
#             return None
#         self.size -= 1
#         return self.storage.pop()

from singly_linked_list_for_stack_usage import LinkedList

# USING LINKED LISTS and TAILS:
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        #adds an item to the top of the stack (aka last in line)
        self.storage.add_to_tail(value)
        self.size += 1

    def pop(self):
        #removes and returns the element at the top of the stack
        if self.size == 0:
            return None
        self.size -= 1
        return self.storage.remove_tail()

