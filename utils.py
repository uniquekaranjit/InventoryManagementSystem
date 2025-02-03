# ----------------------------------------------------------------------------------------------------------------------
# Utility classes required by Main Driver Code 
# Author: Unique Karanjit
# Feb 2, 2025
# ----------------------------------------------------------------------------------------------------------------------

import random
from tabulate import tabulate

# Function to generate a list of random products based on categories and quantity
def generate_random_inventory(categories, noOfProducts):
    """
    Generates a list of random products with unique IDs, randomly selected names 
    from the categories list, and random prices between 50 and 2000.
    
    Args:
    categories (list): List of category names to randomly assign to products.
    noOfProducts (int): The number of products to generate.

    Returns:
    list: A list of dictionaries, each containing product details (id, name, price).
    """
    products = []
    for i in range(noOfProducts):
        product = {
            "id": f"P{i+1:03}",  # Generate unique ID for each product
            "name": random.choice(categories),  # Randomly select a name from categories
            "price": random.randint(50, 2000)  # Random price between 50 and 2000
        }
        products.append(product)
    return products

# Function to print the full inventory as a table
def print_inventory(inventory):
    """
    Prints the entire inventory in a formatted table using the tabulate library.
    
    Args:
    inventory (list): The list of products to display.
    
    """
    print("\n------Full Inventory------\n")
    print(tabulate(inventory, headers="keys", tablefmt="grid"))

# Function to print a hash table (dictionary) as a table

def print_hashTable_as_table(hashTable):
    """
    Prints the content of the given hash table as a formatted table with headers.
    
    Args:
    hashTable (dict): The hash table to display, where each value is a product dictionary.
    """
    items = hashTable.items()  # Get the key-value pairs from the hash table
    formatted_items = [(key, value['name'], value['price']) for key, value in items]

    headers = ['ID', 'Name', 'Price']
    # Use tabulate to print the hash table as a table
    print(tabulate(formatted_items, headers=headers, tablefmt="grid"))
    
# Function to initialize the inventory by inserting products into a hash table and an AVL tree
def initialize_inventory(inventory, hashtable, AVLTree):
    """
    Initializes the inventory by inserting each product into the provided hash table and AVL tree.
    
    Args:
    inventory (list): The list of products to be inserted into the data structures.
    hashtable (HashTable): The hash table to insert the products into.
    AVLTree (AVLTree): The AVL tree to insert the products into, sorted by price.
    """
    for product in inventory:
        hashtable.insert(product["id"], product)   # Insert product into the hash table
        AVLTree.root = AVLTree.insert(AVLTree.root, product["price"], product["name"])  # Insert product into the AVL tree

# Function to generate a single product with specified ID, name, and price
def generate_product(id,name,price):
    """
    Generates a product dictionary with specified ID, name, and price.
    
    Args:
    id (str): The product ID.
    name (str): The product name.
    price (int): The product price.
    
    Returns:
    dict: A dictionary containing the product details.
    """
    return {
            "id": id,
            "name": name,
            "price": price
        }




