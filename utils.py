# ----------------------------------------------------------------------------------------------------------------------
# Utility classes required by Main Driver Code 
# Author: Unique Karanjit
# Feb 2, 2025
# ----------------------------------------------------------------------------------------------------------------------

import random
from tabulate import tabulate
import uuid

# Function to generate a list of random products based on categories and quantity
def generate_random_inventory(categories, noOfProducts):
    """
    Generates a list of random products with prices having 2 decimal places
    """
    if noOfProducts <= 0:
        raise ValueError("Number of products must be positive")
    if noOfProducts > 1000000:  # Set reasonable limit
        raise ValueError("Too many products requested")
    if not categories:
        raise ValueError("Categories list cannot be empty")
    products = []
    for i in range(noOfProducts):
        # Generate price with 2 decimal places between 50 and 2000
        price = round(random.uniform(50, 2000), 2)
        product = {
            "id": str(uuid.uuid4()),
            "name": random.choice(categories),
            "price": price
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
    Prints the hash table contents in a tabulated format with formatted prices
    """
    if not any(bucket for bucket in hashTable.table):
        print("\nInventory is empty!")
        return
        
    products = []
    for bucket in hashTable.table:
        for _, product in bucket:
            if isinstance(product, dict):
                short_id = product.get('id', '')[:8] if product.get('id') else ''
                price = f"${product.get('price', 0):.2f}"
                products.append([
                    short_id,
                    product.get('name', ''),
                    price
                ])

    headers = ['ID', 'Name', 'Price']
    print("\nCurrent Inventory:")
    print(tabulate(products, headers=headers, tablefmt='grid'))

# Function to initialize the inventory by inserting products into a hash table and an AVL tree
def initialize_inventory(inventory, hashTable, avlTree):
    """
    Initialize both data structures with the inventory data.
    """
    if not inventory:
        print("Warning: Empty inventory provided for initialization")
        return
        
    for product in inventory:
        if not all(key in product for key in ['id', 'name', 'price']):
            print(f"Warning: Skipping invalid product data: {product}")
            continue
        hashTable.insert(product["id"], product)
        avlTree.root = avlTree.insert(avlTree.root, product["price"], product["name"])

# Function to generate a single product with specified ID, name, and price
def generate_product(id=None, name=None, price=None):
    """
    Generates a product dictionary with specified ID (or generates a new UUID if None), 
    name, and price.
    
    Args:
    id (str, optional): The product ID. If None, generates a new UUID.
    name (str): The product name.
    price (int): The product price.
    
    Returns:
    dict: A dictionary containing the product details.
    """
    return {
        "id": id if id else str(uuid.uuid4()),
        "name": name,
        "price": price
    }

def insert_product(hashtable, avl_tree):
    """
    Get product details from user and insert into both data structures.
    ID is auto-generated using UUID.
    """
    print("\n=== Insert New Product ===")
    
    # Name validation
    while True:
        name = input("Enter product name: ").strip()
        if not name:
            print("Error: Product name cannot be empty")
            continue
        if len(name) > 50:
            print("Error: Product name too long (maximum 50 characters)")
            continue
        if not any(c.isalnum() for c in name):
            print("Error: Product name must contain at least one letter or number")
            continue
        break
        
    # Price validation
    while True:
        try:
            price = float(input("Enter product price: "))
            # Check if price has more than 2 decimal places
            if abs(round(price, 2) - price) > 0.00001:
                print("Error: Price cannot have more than 2 decimal places")
                continue
            if price <= 0:
                print("Error: Price must be greater than 0")
                continue
            if price > 1000000:
                print("Error: Price exceeds maximum limit of $1,000,000")
                continue
            price = round(price, 2)
            break
        except ValueError:
            print("Please enter a valid number for price")
    
    new_product = {
        "name": name,
        "price": price
    }
    
    new_product = hashtable.insert(None, new_product)
    avl_tree.root = avl_tree.insert(avl_tree.root, price, new_product["name"])
    
    print("\nProduct added successfully!")
    print(f"Generated ID: {new_product['id'][:8]}")



