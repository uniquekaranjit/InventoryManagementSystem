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
from utils import generate_product

# Driver Code 
if __name__=="__main__":
    print ("\n*** Welcome to Inventory Management System ***\n\n")

    categories = ["Phone","Charger","Headphones","Laptop","Ipad"]
    noofProducts = 20

    # Generate Random Inventory 
    inventory = generate_random_inventory(categories,noofProducts) 
    # inventory will never be used later. 

    # Initialize Hash Map and AVL 
    hashTable = HashTable()
    avlTree = AVLTree()
    initialize_inventory(inventory,hashTable,avlTree)

    # Print Inventory 
    print_inventory(inventory)

    while True:
        print("\nPlease enter your option.\n")
        print("1. Insert New Item Based on Product ID")
        print("2. Delete Item Based on Product ID")
        print("3. Retrieve Item Based on Product ID")
        print("4. Print Current Inventory")
        print("5. Exit")

        print("\n\n======================================")
        choice = input("\nEnter your choice (1/2/3/4/5): ")

        if choice == '1':
            item_id = input("\nEnter the product id of the item to insert: ")
            item_name = input("Enter the product name of the item to insert: ")
            item_price = int(input("Enter the product price of the item to insert: "))
          
            product = generate_product(item_id, item_name, item_price)
            hashTable.insert(item_id, product)
            avlTree.root = avlTree.insert(avlTree.root, item_price, item_name)
            print(f"Product inserted with id: {item_id} ")
        elif choice == '2':
            item_id = input("Enter the product id of the item to delete: ")
            hashTable.delete(item_id)
            print(f"Retrieve {item_id} after deletion:", hashTable.get(item_id))

        elif choice == '3':
            item_id = input("\nEnter the product id of the item to retrieve: ")
            if(hashTable.get(item_id)!=None):
                print("Retrieved Product ID:", hashTable.get(item_id).get("id"))
                print("Retrieved Product Name:", hashTable.get(item_id).get("name"))
                print("Retrieved Product Price:", hashTable.get(item_id).get("price"))
            else:
                print(f"Product not found with ID {item_id}")
        
        elif choice == '4':
            print_hashTable_as_table(hashTable)

        elif choice == '5':
            print("\nExiting the Inventory Management system.")
            break
        else:
            print("Invalid choice, please try again.")

