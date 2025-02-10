import unittest
from AVLTree import AVLTree
from hashtable import HashTable
from utils import generate_random_inventory, initialize_inventory
import random

class RegressionTest(unittest.TestCase):
    def setUp(self):
        self.hashTable = HashTable()
        self.avlTree = AVLTree()
        self.categories = ["Laptop", "Phone", "Tablet"]
        
    def test_insert_and_balance(self):
        # Test inserting items and checking AVL balance
        products = [
            {"id": "L001", "name": "Budget Laptop", "price": 500.00},
            {"id": "L002", "name": "Premium Laptop", "price": 1500.00},
            {"id": "L003", "name": "Gaming Laptop", "price": 2000.00},
            {"id": "L004", "name": "Ultra Laptop", "price": 2500.00},
            {"id": "L005", "name": "Basic Laptop", "price": 300.00},
        ]
        
        for product in products:
            self.avlTree.root = self.avlTree.insert(self.avlTree.root, product["price"], product)
            self.assertTrue(self.avlTree.is_balanced(), "Tree should remain balanced after insertion")
            
    def test_random_inventory(self):
        # Test generating and initializing random inventory
        try:
            inventory = generate_random_inventory(self.categories, 5)
            initialize_inventory(inventory, self.hashTable, self.avlTree)
            self.assertTrue(self.avlTree.is_balanced(), "Tree should be balanced after initialization")
        except Exception as e:
            self.fail(f"Random inventory generation failed: {str(e)}")
            
    def test_hash_table_operations(self):
        # Test basic hash table operations
        product = {"id": "L001", "name": "Test Laptop", "price": 1000.00}
        self.hashTable.insert(product["id"], product)
        
        # Test retrieval
        retrieved = self.hashTable.find_by_partial_id("L001")
        self.assertIsNotNone(retrieved, "Should find product by ID")
        self.assertEqual(retrieved["price"], 1000.00)
        
        # Test deletion
        self.hashTable.delete("L001")
        retrieved = self.hashTable.find_by_partial_id("L001")
        self.assertIsNone(retrieved, "Product should be deleted")

    def test_avl_rotations(self):
        # Test left-left case
        products = [
            {"id": "L003", "name": "Laptop 3", "price": 3000.00},
            {"id": "L002", "name": "Laptop 2", "price": 2000.00},
            {"id": "L001", "name": "Laptop 1", "price": 1000.00},
        ]
        for product in products:
            self.avlTree.root = self.avlTree.insert(self.avlTree.root, product["price"], product)
        self.assertTrue(self.avlTree.is_balanced())

        # Test right-right case
        self.avlTree = AVLTree()  # Reset tree
        products = [
            {"id": "L001", "name": "Laptop 1", "price": 1000.00},
            {"id": "L002", "name": "Laptop 2", "price": 2000.00},
            {"id": "L003", "name": "Laptop 3", "price": 3000.00},
        ]
        for product in products:
            self.avlTree.root = self.avlTree.insert(self.avlTree.root, product["price"], product)
        self.assertTrue(self.avlTree.is_balanced())

    def test_partial_id_search(self):
        # Test partial ID search functionality
        products = [
            {"id": "LAP001", "name": "Laptop 1", "price": 1000.00},
            {"id": "LAP002", "name": "Laptop 2", "price": 2000.00},
            {"id": "PHN001", "name": "Phone 1", "price": 500.00},
        ]
        
        # Insert and verify each product
        for product in products:
            self.hashTable.insert(product["id"], product)
            # Verify immediate retrieval with exact ID
            retrieved = self.hashTable.find_by_partial_id(product["id"])
            self.assertIsNotNone(retrieved, f"Should find product with exact ID {product['id']}")
        
        # Test partial match with multiple results (should return None)
        lap_result = self.hashTable.find_by_partial_id("LAP")
        self.assertIsNone(lap_result, "Should return None for multiple matches")
        
        # Test exact ID match
        lap001_result = self.hashTable.find_by_partial_id("LAP001")
        self.assertIsNotNone(lap001_result, "Should find exact product LAP001")
        self.assertEqual(lap001_result["price"], 1000.00)
        
        # Test non-existent ID
        none_result = self.hashTable.find_by_partial_id("NONEXISTENT")
        self.assertIsNone(none_result, "Should return None for non-existent ID")

    def test_edge_cases(self):
        # Test empty tree operations
        self.assertIsNone(self.avlTree.root)
        
        # Test invalid product insertion
        invalid_product = {"id": "", "name": "", "price": -100.00}
        try:
            self.hashTable.insert(invalid_product["id"], invalid_product)
            self.fail("Should not allow empty ID")
        except ValueError:
            pass

        # Test deletion from empty hash table
        result = self.hashTable.delete("nonexistent")
        self.assertFalse(result, "Deleting from empty hash table should return False")

    def test_price_range_edge_cases(self):
        """Test edge cases for product prices"""
        products = [
            {"id": "MIN001", "name": "Minimum Price", "price": 0.01},
            {"id": "MAX001", "name": "Maximum Price", "price": 999999.99},
        ]
        
        # Valid prices should be accepted
        for product in products:
            self.hashTable.insert(product["id"], product)
            retrieved = self.hashTable.find_by_partial_id(product["id"])
            self.assertIsNotNone(retrieved, f"Should accept valid price for {product['name']}")
        
        # Invalid price should raise ValueError
        invalid_product = {"id": "NEG001", "name": "Negative Price", "price": -1.00}
        with self.assertRaises(ValueError):
            self.hashTable.insert(invalid_product["id"], invalid_product)

    def test_random_data_balance(self):
        """Test AVL tree balance with random data"""
        prices = random.sample(range(1, 10000), 20)
        for i, price in enumerate(prices):
            product = {
                "id": f"RAND{i:03d}",
                "name": f"Random Product {i}",
                "price": float(price)
            }
            self.avlTree.root = self.avlTree.insert(self.avlTree.root, product["price"], product)
        
        self.assertTrue(self.avlTree.is_balanced(), "Tree should remain balanced after random insertions")

    def test_data_consistency(self):
        """Test consistency between hash table and AVL tree"""
        test_product = {"id": "TEST001", "name": "Test Product", "price": 999.99}
        
        # Insert in both structures
        self.hashTable.insert(test_product["id"], test_product)
        self.avlTree.root = self.avlTree.insert(self.avlTree.root, test_product["price"], test_product)
        
        # Verify retrieval
        hash_result = self.hashTable.find_by_partial_id("TEST001")
        self.assertIsNotNone(hash_result, "Should retrieve from hash table")
        self.assertEqual(hash_result["price"], test_product["price"])
        
        # Test deletion
        self.assertTrue(self.hashTable.delete("TEST001"), "Should successfully delete from hash table")
        self.assertTrue(self.avlTree.is_balanced(), "Tree should remain balanced after operations")

    def test_id_collisions(self):
        """Test handling of similar IDs"""
        similar_products = [
            {"id": "LAPTOP001", "name": "Laptop 1", "price": 1000.00},
            {"id": "LAPTOP002", "name": "Laptop 2", "price": 1500.00},
            {"id": "LAPTOP003", "name": "Laptop 3", "price": 2000.00}
        ]
        
        # Insert all products
        for product in similar_products:
            self.hashTable.insert(product["id"], product)
            
        # Partial search should return None for multiple matches
        result = self.hashTable.find_by_partial_id("LAPTOP")
        self.assertIsNone(result, "Should return None for multiple matches")
        
        # Exact ID should still work
        exact_result = self.hashTable.find_by_partial_id("LAPTOP001")
        self.assertIsNotNone(exact_result, "Should find exact ID match")
        self.assertEqual(exact_result["price"], 1000.00)

if __name__ == '__main__':
    unittest.main() 