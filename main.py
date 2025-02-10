# ----------------------------------------------------------------------------------------------------------------------
# Hash Table Driver Code
# Author: Unique Karanjit
# Feb 2, 2025
# ----------------------------------------------------------------------------------------------------------------------

# Import necessary dependencies.
from hashtable import HashTable
from AVLTree import AVLTree
from utils import generate_random_inventory
from utils import print_inventory
from utils import initialize_inventory
from utils import print_hashTable_as_table
from utils import insert_product

# Define maximum inventory size
MAX_INVENTORY_SIZE = 1000000

def main():
    try:
        # Initialize data structures
        hashTable = HashTable()
        avlTree = AVLTree()
        
        # Initialize with some random data
        categories = ["Laptop", "Phone", "Tablet", "Watch", "Camera", "Headphones", "Speaker", "Charger"]
        try:
            inventory = generate_random_inventory(categories, 5)
            initialize_inventory(inventory, hashTable, avlTree)
        except ValueError as e:
            print(f"Error initializing inventory: {str(e)}")
            return

        while True:
            try:
                print("\nPlease enter your option.\n")
                print("1. Insert New Item Based on Product ID")
                print("2. Delete Item Based on Product ID")
                print("3. Retrieve Item Based on Product ID")
                print("4. Print Current Inventory")
                print("5. Find Cheapest Product")
                print("6. Find Most Expensive Product")
                print("7. Find Products in Price Range")
                print("8. View Products Sorted by Price")
                print("9. Exit")

                print("\n======================================")
                choice = input("\nEnter your choice (1-9): ").strip()

                if not choice.isdigit() or not (1 <= int(choice) <= 9):
                    print("Please enter a number between 1 and 9")
                    continue

                if choice == '1':
                    current_size = sum(len(bucket) for bucket in hashTable.table)
                    if current_size >= MAX_INVENTORY_SIZE:
                        print(f"\nError: Maximum inventory size ({MAX_INVENTORY_SIZE}) reached")
                        continue
                    insert_product(hashTable, avlTree)
                    
                elif choice == '2':
                    if not any(bucket for bucket in hashTable.table):
                        print("\nInventory is empty!")
                        continue
                        
                    item_id = input("Enter the first few characters of product ID to delete: ").strip()
                    if not item_id:
                        print("ID cannot be empty")
                        continue
                        
                    product = hashTable.find_by_partial_id(item_id)
                    if product:
                        confirm = input(f"\nAre you sure you want to delete '{product['name']}' priced at ${product['price']:.2f}? (y/n): ").lower().strip()
                        if confirm != 'y':
                            print("Deletion cancelled")
                            continue
                        
                        product_price = product['price']
                        product_name = product['name']
                        
                        hash_result = hashTable.delete(product['id'])
                        avlTree.root = avlTree.delete(avlTree.root, product_price)
                        
                        print(f"Product '{product_name}' with ID starting with '{item_id}' has been deleted.")
                        
                        if hash_result and avlTree.root:
                            if not avlTree.is_balanced():
                                print("\nWarning: AVL tree is not balanced!")
                    
                elif choice == '3':
                    if not any(bucket for bucket in hashTable.table):
                        print("\nInventory is empty!")
                        continue
                        
                    item_id = input("\nEnter the first few characters of product ID to retrieve: ").strip()
                    product = hashTable.find_by_partial_id(item_id)
                    if product:
                        print("\nProduct Details:")
                        print(f"ID: {product['id']}")
                        print(f"Name: {product['name']}")
                        print(f"Price: ${product['price']:.2f}")
                    
                elif choice == '4':
                    print_hashTable_as_table(hashTable)
                    
                elif choice == '5':
                    if not avlTree.root:
                        print("\nNo products in inventory!")
                        continue
                    cheapest = avlTree.find_cheapest()
                    print(f"\nCheapest Product:")
                    print(f"Name: {cheapest['name']}")
                    print(f"Price: ${cheapest['price']:.2f}")
                    
                elif choice == '6':
                    if not avlTree.root:
                        print("\nNo products in inventory!")
                        continue
                    most_expensive = avlTree.find_most_expensive()
                    print(f"\nMost Expensive Product:")
                    print(f"Name: {most_expensive['name']}")
                    print(f"Price: ${most_expensive['price']:.2f}")
                    
                elif choice == '7':
                    if not avlTree.root:
                        print("\nNo products in inventory!")
                        continue
                        
                    try:
                        while True:
                            min_price = float(input("Enter minimum price: "))
                            if abs(round(min_price, 2) - min_price) > 0.00001:
                                print("Error: Price cannot have more than 2 decimal places")
                                continue
                            if min_price < 0:
                                print("Error: Minimum price cannot be negative")
                                continue
                            if min_price > 1000000:
                                print("Error: Price exceeds maximum limit of $1,000,000")
                                continue
                            min_price = round(min_price, 2)
                            break

                        while True:
                            max_price = float(input("Enter maximum price: "))
                            if abs(round(max_price, 2) - max_price) > 0.00001:
                                print("Error: Price cannot have more than 2 decimal places")
                                continue
                            if max_price < 0:
                                print("Error: Maximum price cannot be negative")
                                continue
                            if max_price > 1000000:
                                print("Error: Price exceeds maximum limit of $1,000,000")
                                continue
                            if max_price < min_price:
                                print(f"Error: Maximum price (${max_price:.2f}) cannot be less than minimum price (${min_price:.2f})")
                                continue
                            if max_price == min_price:
                                print(f"\nNote: Searching for exact price match at ${max_price:.2f}")
                            max_price = round(max_price, 2)
                            break

                        products = avlTree.find_products_in_range(min_price, max_price)
                        if not products:
                            print(f"\nNo products found between ${min_price:.2f} and ${max_price:.2f}")
                        else:
                            print(f"\nProducts between ${min_price:.2f} and ${max_price:.2f}:")
                            for product in products:
                                print(f"Name: {product['name']}, Price: ${product['price']:.2f}")
                                
                    except ValueError:
                        print("Please enter valid numbers for prices")
                    
                elif choice == '8':
                    if not avlTree.root:
                        print("\nNo products in inventory!")
                        continue
                        
                    sort_order = input("Sort in descending order? (y/n): ").lower().strip()
                    while sort_order not in ['y', 'n']:
                        print("Please enter 'y' for yes or 'n' for no")
                        sort_order = input("Sort in descending order? (y/n): ").lower().strip()
                        
                    products = avlTree.get_sorted_products(descending=sort_order == 'y')
                    if not products:
                        print("No products to display")
                        continue
                    
                    print("\nProducts Sorted by Price:")
                    for product in products:
                        print(f"Name: {product['name']}, Price: ${product['price']:.2f}")
                    
                elif choice == '9':
                    print("\nExiting the Inventory Management system.")
                    break

            except Exception as e:
                print(f"An error occurred: {str(e)}")
                print("Please try again.")

    except Exception as e:
        print(f"Fatal error: {str(e)}")
        print("Program terminated.")

if __name__ == "__main__":
    main()



