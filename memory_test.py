import psutil
import time
import matplotlib.pyplot as plt
from datetime import datetime
from hashtable import HashTable
from AVLTree import AVLTree
from utils import generate_random_inventory

def test_memory_usage():
    """Test memory usage with different data sizes"""
    # Initialize data structures
    hashTable = HashTable()
    avlTree = AVLTree()
    
    # Test sizes
    sizes = [100, 500, 1000, 5000, 10000, 50000, 100000]
    memory_usage = []
    categories = ["Laptop", "Phone", "Tablet", "Watch", "Camera", "Headphones"]
    
    print("\nStarting Memory Usage Test...")
    
    for size in sizes:
        # Record memory before
        process = psutil.Process()
        memory_before = process.memory_info().rss / (1024 * 1024)  # MB
        
        print(f"\nTesting with {size} items...")
        
        # Generate and insert data
        inventory = generate_random_inventory(categories, size)
        for product in inventory:
            hashTable.insert(product["id"], product)
            avlTree.root = avlTree.insert(avlTree.root, product["price"], product["name"])
            
        # Record memory after
        memory_after = process.memory_info().rss / (1024 * 1024)  # MB
        memory_used = memory_after - memory_before
        memory_usage.append(memory_used)
        
        print(f"Memory used for {size} items: {memory_used:.2f} MB")
        
    # Plot results
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, memory_usage, marker='o')
    plt.title('Memory Usage vs Data Size')
    plt.xlabel('Number of Items')
    plt.ylabel('Memory Usage (MB)')
    plt.grid(True)
    
    # Add value labels on points
    for i, v in enumerate(memory_usage):
        plt.text(sizes[i], v, f'{v:.1f}MB', ha='center', va='bottom')
    
    plt.tight_layout()
    plt.savefig('evidences/memory_test_results.png')
    plt.close()
    
    print("\nMemory test completed!")
    print("Results have been saved to 'evidences/memory_test_results.png'")
    
    # Print summary statistics
    print("\nSummary:")
    print(f"Maximum memory usage: {max(memory_usage):.2f} MB")
    print(f"Average memory usage: {sum(memory_usage)/len(memory_usage):.2f} MB")
    print(f"Memory usage per item: {sum(memory_usage)/sum(sizes):.4f} MB")

if __name__ == "__main__":
    test_memory_usage() 