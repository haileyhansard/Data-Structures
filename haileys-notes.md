# Runtime Complexity
> an objective way to measure the efficiency of code/algorithms

# Classifications:
#-------------------------------------
## CONSTANT TIME: 
- Definition: an operation that takes the same amount of time regardless of input size.
- ex: list indexing. when we have a list and we access it by index.
commands = ['n', 's', 'e', 'w']
commands[1] #constant time operation, it doesnt depend on the size of the input that we are acting on, the input being the number of elements in the list. It doesn't matter how long the list is, it will always take the same amount of time to find that index.

- ex: accessing a dictionay value by key


`rooms = {"outside": Room(...), ... }
rooms["outside"] //accessing this element from the dictionary - the runtime doesnt depend on the number of elements in the dictionary, it will be the same`



#-------------------------------------
## LINEAR TIME:
- An operation that does depend on the size of the input; the time the operation takes increases linearly with the input size.
- DOES depend on the number of elements in the commands list
- ex: for loops.

`for command in commands:
    #do something
    #adding 1 to list size increases number of loop iterations by c for some constant (could be 1, 5, 10, but some constant amount)`

for key, value in rooms.items(): #linear time operation

#-------------------------------------
## QUADRATIC TIME:
- An operation that does depend on the size of the input; the time the operation takes increases quadratically with input size. As input size increases, the runtime will grow at a faster rate.

- ex: print out every combination of pairs of commands for our command list

`for x in commands: # 6 commands
    for y in commands: #6 commands
        print (x, y)
        (n,n), (n,s), (n, e), (n, w)
        (s,n), (s, s), (s, e), (s, w) ...
        (e,n), (e, s) ...
        (w,n), ...
        #it would print out 36 command pairs. (6 commands x 6 commands)`


#-------------------------------------
## LINKED LISTS
 `class Node:
 value
 next`
#-------------------------------------
## STACKS:
- Last In First Out. LIFO
- think about it like a stack of plates.
- If you add new plates to the top of the stack, and you can easily take one plate off the top of stack, this is Last In First Out. The last one added to the stack of plates is the first one taken off the stack.

#-------------------------------------
## QUEUES:
- First In First Out.  FIFO
- Like a line at the pharmacy. The first in line gets helped, then is first to leave the line.

#-------------------------------------
## RECURSION:
- Another way of thinking about iteration. 
- example: calling the function again in order to move the search along
- (1) we need at least one base case. this will be the stopping criteria. When we encouter this, we stop the recursion.
- (2) we need a way to move closer to a base case.
- iterative solutions have these 2 requirements as well, just spelled out differently.
- in iterative scenario: we are returning (True) when we find the target, or we have iterated through the entire array and did not find target (False). Looping aspect is more front and center in the iterative scenario.
    def search(arr, target):
        for n in arr:
            if n == target:
                return True
        return False

    arr = [5, 17, 8, 9, 3, 14]
    print(serach(arr, 3))

- in recursive scenario: we are going to flip it on its head. If array starts out empty, we return False because target is not in there. If last value is target, stop and return True. If not, repeat the search process on the next value, return if True. If not, repeat the search value on the next value, return if True.
    def search(arr, target):
        if len(arr) == 0:
            return False
        if arr[-1] == target:
            return True
        return search(arr[:-1], target)
        
    arr = [5, 17, 8, 9, 3, 14]
    print(serach(arr, 3))