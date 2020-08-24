class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def find(self, value):
        # start at the head
        # iterate over the list
        # find value
        # return the node with that value
        current = self.head
        while current is not None:
            if current.value == value:
                return current
            current = current.next    
        # for hash tables, you'll get a key
        # go through each node and see if keys match
        # and if they do, return the value

    def delete(self, value):
        # first find it, then delete it
        current = self.head

        if current.value == value:
            self.head = current.next
            return current

        previous = current
        current = current.next    

        while current is not None:
            if current.value == value:
                previous.next = current.next
                return current
            else:
                previous = current
                current = current.next    
        # if you get this far and haven't found the node
        return None        

    def insert_at_head(self, node):
        node.next = self.head
        self.head = node              


"""
Hashtable notes
If you have multiple values at each index, what do you do? 
-Resize. Take all these values, make hash map way bigger, and 
distribute the values again.

How do you know when to resize? 
-Calculate load factor: 
number of elements (total) / number of slots (indices in the hashtable, capacity)

Typically, if you get to load factor of 0.7, you need to resize.
-double the size of your hash map
-re-put everything in the hash map

Amortized runtime: because it happens so rarely, we don't really count it.
So even though resizing the hash map and putting everything in it again
is linear time, overall we can say hashtable runs on constant time still.

What if you delete a bunch of stuff? And end up with a hash table that
has a lot of free space? In the industry, that's a problem because
wasted space is wasted money.
-if load factor < 0.2, half the size of the hash map.
-re-put everything in the hash map

On put and delete, check load factor!
"""