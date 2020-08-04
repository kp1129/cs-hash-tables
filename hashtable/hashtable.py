class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8

class LinkedList:
    def __init__(self):
        self.head = None

    def find(self, key):
        current = self.head

        while current is not None:
            if current.key == key:
                return current
            current = current.next    

        return None    

    def add_to_head(self, node):
        node.next = self.head
        self.head = node        

    def remove_by_key(self, key):
   
        current = self.head

        # if the head holds the key
        if current.key == key:
            self.head = self.head.next
            return

        # else, search the linked list while 
        # keeping track of previous node  
        previous = None
        while current is not None:
            if current.key == key:
                previous.next = current.next
                return 
            previous = current
            current = current.next    

        # if no key matched
        return "warning: no such key" 


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here        
        self.capacity = capacity
        self.elements_count = 0
        self.storage = [None] * capacity


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return self.elements_count / self.capacity

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        self.FNV_prime = 1099511628211
        self.hash = 14695981039346656037

        for char in key:
            self.hash = self.hash * self.FNV_prime
            self.hash = self.hash ^ ord(char)

        return self.hash    

    # def djb2(self, key):
    #     """
    #     DJB2 hash, 32-bit

    #     Implement this, and/or FNV-1.
    #     """
    #     # Your code here


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # convert key and value to HashTableEntry instance
        node = HashTableEntry(key, value)
        
        # hash the key
        ix = self.hash_index(key)

        if self.storage[ix] is None: 
            ll = LinkedList()
            ll.head = node
            self.storage[ix] = ll
            # increment elements_count
            self.elements_count += 1
            return
        # if that ix is not empty, iterate over ll to make sure there 
        # is no matching key; if there is, overwrite its value, if not, insert.
        found = self.storage[ix].find(key)
        if found is not None:
            found.value = value
            return
        self.storage[ix].add_to_head(node)
        # increment elements_count
        self.elements_count += 1    


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # get index
        ix = self.hash_index(key)
        # go to that index and delete the node
        result = self.storage[ix].remove_by_key(key)
        if type(result) == str:
            print("warning: no such key")
        else:
            # decrement elements_count
            self.elements_count -= 1        


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # get index
        ix = self.hash_index(key)
        # go to this index and find the key
        found = self.storage[ix].find(key)
        if found is not None:
            return found.value
        return None    
 


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        self.new_storage = [None] * new_capacity
        for i in self.storage:
            self.new_storage[i] = self.storage[i]
        self.capacity = new_capacity
        self.storage = self.new_storage



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")

    # ht = HashTable(8)

    # ht.put("key-0", "val-0")
    # # ht.put("key-1", "val-1")
    # # ht.put("key-2", "val-2")

    # return_value = ht.get("key-0")
    # print('this should return true', return_value == "val-0")

