# ----------------------------------------------------------------------------------------------------------------------
# Hash Table Implementation 
# Author: Unique Karanjit
# Jan 17, 2025
# This portion is implemented as part of Phase 1 @Unique Karanjit
# ----------------------------------------------------------------------------------------------------------------------


class HashTable:
    """
    A simple hash table implementation using separate chaining for collision handling.
    
    This hash table stores key-value pairs, where the keys are hashed to determine their 
    placement in the table. If collisions occur (multiple keys hashing to the same index), 
    the values are stored in a list at that index.
    """

    def __init__(self, size=100):
        """
        Initializes the hash table with a given size.

        :param size: The number of buckets in the hash table (default is 100).
        """
        self.table = [[] for _ in range(size)]  # Create a list of empty lists for separate chaining.

    def _hash(self, key):
        """
        Computes the hash index for a given key.

        :param key: The key to be hashed.
        :return: The index in the table where the key-value pair should be stored.
        """
        return hash(key) % len(self.table)  # Ensure the index stays within the table's size.

    def insert(self, key, product):
        """
        Inserts a key-value pair into the hash table. If the key already exists, 
        its value is updated.

        :param key: The key associated with the value.
        :param product: The value to be stored.
        """
        index = self._hash(key)  # Get the index for the key.
        for i, (k, v) in enumerate(self.table[index]):  # Iterate over the bucket to check for existing key.
            if k == key:
                self.table[index][i] = (key, product)  # Update the value if the key already exists.
                return
            print(key,product)
        self.table[index].append((key, product))  # Otherwise, append a new key-value pair.

    def get(self, key):
        """
        Retrieves the value associated with the given key.

        :param key: The key whose value is to be retrieved.
        :return: The associated value, or None if the key is not found.
        """
        index = self._hash(key)  # Get the index for the key.
        for k, v in self.table[index]:  # Iterate through the bucket.
            if k == key:
                return v  # Return the value if the key is found.
        return None  # Return None if the key is not found.

    def delete(self, key):
        """
        Deletes a key-value pair from the hash table.

        :param key: The key to be removed.
        :return: True if the key was found and deleted, False otherwise.
        """
        index = self._hash(key)  # Get the index for the key.
        for i, (k, _) in enumerate(self.table[index]):  # Iterate through the bucket.
            if k == key:
                del self.table[index][i]  # Remove the key-value pair if found.
                return True  # Return True to indicate successful deletion.
        return False  # Return False if the key was not found.
    
    def items(self):
        """
        Retrieves all key-value pairs from the hash table.

        :return: A list of tuples containing all the key-value pairs.
        """
        all_items = []
        for bucket in self.table:  # Iterate through each bucket in the table.
            all_items.extend(bucket)  # Add all key-value pairs from the current bucket to the list.
        return all_items
