import time
import random
import matplotlib.pyplot as plt
from utils import generate_random_inventory
from hashtable import HashTable
from AVLTree import AVLTree

class PerformanceTest:
    def __init__(self):
        self.categories = ["Laptop", "Phone", "Tablet", "Watch", "Camera", "Headphones"]
        self.test_sizes = [100, 500, 1000, 5000, 10000, 100000]
        self.results = {
            'insert': {'sizes': [], 'times': []},
            'search': {'sizes': [], 'times': []},
            'range_search': {'sizes': [], 'times': []},
            'delete': {'sizes': [], 'times': []}
        }

    def test_insertion(self, size):
        """Test insertion performance"""
        hashTable = HashTable()
        avlTree = AVLTree()
        
        start_time = time.perf_counter()
        
        inventory = generate_random_inventory(self.categories, size)
        for product in inventory:
            hashTable.insert(product["id"], product)
            avlTree.root = avlTree.insert(avlTree.root, product["price"], product["name"])
            
        end_time = time.perf_counter()
        return end_time - start_time

    def test_search(self, size):
        """Test search performance"""
        hashTable = HashTable()
        inventory = generate_random_inventory(self.categories, size)
        
        # Insert data first
        for product in inventory:
            hashTable.insert(product["id"], product)
        
        # Test search performance
        start_time = time.perf_counter()
        for _ in range(100):  # Perform 100 random searches
            search_id = random.choice(inventory)["id"][:4]
            hashTable.find_by_partial_id(search_id)
        end_time = time.perf_counter()
        
        return (end_time - start_time) / 100  # Average search time

    def test_range_search(self, size):
        """Test range search performance"""
        avlTree = AVLTree()
        inventory = generate_random_inventory(self.categories, size)
        
        # Insert data first
        for product in inventory:
            avlTree.root = avlTree.insert(avlTree.root, product["price"], product["name"])
        
        # Test range search performance
        start_time = time.perf_counter()
        for _ in range(50):  # Perform 50 random range searches
            min_price = random.uniform(50, 1000)
            max_price = min_price + random.uniform(100, 500)
            avlTree.find_products_in_range(min_price, max_price)
        end_time = time.perf_counter()
        
        return (end_time - start_time) / 50  # Average range search time

    def run_all_tests(self):
        """Run all performance tests"""
        for size in self.test_sizes:
            print(f"\nTesting with size: {size}")
            
            # Test insertion
            insert_time = self.test_insertion(size)
            self.results['insert']['sizes'].append(size)
            self.results['insert']['times'].append(insert_time)
            print(f"Insertion time: {insert_time:.4f} seconds")
            
            # Test search
            search_time = self.test_search(size)
            self.results['search']['sizes'].append(size)
            self.results['search']['times'].append(search_time)
            print(f"Average search time: {search_time:.4f} seconds")
            
            # Test range search
            range_time = self.test_range_search(size)
            self.results['range_search']['sizes'].append(size)
            self.results['range_search']['times'].append(range_time)
            print(f"Average range search time: {range_time:.4f} seconds")

    def plot_results(self):
        """Plot performance results"""
        plt.figure(figsize=(12, 8))
        
        operations = ['insert', 'search', 'range_search']
        markers = ['o', 's', '^']
        
        for op, marker in zip(operations, markers):
            plt.plot(
                self.results[op]['sizes'],
                self.results[op]['times'],
                marker=marker,
                label=f'{op.replace("_", " ").title()}'
            )
        
        plt.xlabel('Dataset Size')
        plt.ylabel('Time (seconds)')
        plt.title('Performance Analysis')
        plt.legend()
        plt.grid(True)
        plt.savefig('evidences/performance_results.png')
        plt.close()

def main():
    # Run performance tests
    tester = PerformanceTest()
    tester.run_all_tests()
    tester.plot_results()
    
    print("\nPerformance testing completed. Results saved to 'evidences/performance_results.png'")

if __name__ == "__main__":
    main() 