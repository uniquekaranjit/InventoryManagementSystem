# ----------------------------------------------------------------------------------------------------------------------
# Hash Table Implementation 
# Author: Unique Karanjit
# Jan 17, 2025
# This portion is implemented as part of Phase 1 @Unique Karanjit
# ----------------------------------------------------------------------------------------------------------------------

import uuid  # Add this at the top of the file

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
        if size <= 0:
            raise ValueError("Hash table size must be positive")
        self.size = size
        self.table = [[] for _ in range(size)]  # Create a list of empty lists for separate chaining.

    def _hash(self, key):
        """
        Computes the hash index for a given key.

        :param key: The key to be hashed.
        :return: The index in the table where the key-value pair should be stored.
        """
        if not key:
            raise ValueError("Key cannot be None or empty")
        return hash(str(key)) % self.size

    def insert(self, key, value):
        """
        Insert a key-value pair into the hash table.
        If key is None, generates a new UUID.
        """
        if not isinstance(value, dict):
            raise ValueError("Value must be a dictionary")
            
        # Generate new UUID if key is None
        if key is None:
            key = str(uuid.uuid4())
            value['id'] = key
            
        # Validate product data
        if 'name' not in value or not value['name']:
            raise ValueError("Product must have a name")
        if 'price' not in value:
            raise ValueError("Product must have a price")
        if not isinstance(value['price'], (int, float)) or value['price'] <= 0:
            raise ValueError("Invalid price value")
            
        index = self._hash(key)
        
        # Update if key exists
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return value
                
        # Insert new key-value pair
        self.table[index].append((key, value))
        return value

    def get(self, key):
        """
        Retrieves a value by key.
        """
        if not key:
            return None
            
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def delete(self, key):
        """
        Deletes a key-value pair from the hash table.
        
        :param key: The key to delete
        :return: True if deleted, False if not found
        """
        if not key:
            return False
            
        index = self._hash(key)
        for i, (k, _) in enumerate(self.table[index]):
            if k == key:
                self.table[index].pop(i)
                return True
        return False

    def items(self):
        """
        Retrieves all key-value pairs from the hash table.

        :return: A list of tuples containing all the key-value pairs.
        """
        all_items = []
        for bucket in self.table:  # Iterate through each bucket in the table.
            all_items.extend(bucket)  # Add all key-value pairs from the current bucket to the list.
        return all_items

    def find_by_partial_id(self, partial_id):
        """
        Finds a product using a partial UUID match.
        Returns None if no match or multiple matches found.
        """
        if not partial_id:
            print("Error: ID cannot be empty")
            return None
            
        partial_id = partial_id.strip().lower()
        
        # Validate input length
        if len(partial_id) < 2:
            print("Please enter at least 2 characters for ID search")
            return None
            
        # Check for invalid characters
        if not all(c.isalnum() for c in partial_id):
            print("ID should only contain letters and numbers")
            return None
        
        matches = []
        for bucket in self.table:
            for key, product in bucket:
                if str(key).lower().startswith(partial_id):
                    matches.append(product)
        
        if not matches:
            print(f"No products found with ID starting with '{partial_id}'")
            return None
            
        if len(matches) > 1:
            print("\nMultiple products found with ID starting with '{partial_id}':")
            for product in matches:
                print(f"ID: {product['id'][:8]} | Name: {product['name']} | Price: ${product['price']:.2f}")
            print("\nPlease provide more characters of the ID to narrow down the search.")
            return None
        
        return matches[0]
