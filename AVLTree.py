# ----------------------------------------------------------------------------------------------------------------------
# AVL Tree Implementation 
# Author: Unique Karanjit
# Jan 17, 2025
# This portion is implemented as part of Phase 1 @Unique Karanjit
# ----------------------------------------------------------------------------------------------------------------------
class AVLNode:
    """
    Represents a node in an AVL tree.

    Each node stores a product with its price, as well as pointers to its left and right children.
    The height attribute is used to maintain AVL tree balance.
    """

    def __init__(self, price, product):
        """
        Initializes an AVL tree node.

        :param price: The price of the product (used as the sorting key).
        :param product: The product associated with this price.
        """
        self.price = price  # Key used for ordering nodes.
        self.product = product  # Product information stored in the node.
        self.height = 1  # Initial height of the node (leaf nodes have height 1).
        self.left = None  # Pointer to the left child.
        self.right = None  # Pointer to the right child.


class AVLTree:
    """
    An AVL Tree implementation that maintains balance during insertions.

    The tree automatically rebalances itself to ensure efficient search, insert, 
    and delete operations (O(log N) complexity).
    """

    def __init__(self):
        """
        Initializes an empty AVL tree.
        """
        self.root = None  # The root of the AVL tree.

    def insert(self, root, price, product):
        """
        Inserts a new product into the AVL tree, maintaining balance.

        :param root: The root of the current subtree.
        :param price: The price of the product (used as the key).
        :param product: The product to be inserted.
        :return: The new root of the subtree after insertion and balancing.
        """
        if not root:
            return AVLNode(price, product)  # Create a new node if the subtree is empty.

        if price < root.price:
            root.left = self.insert(root.left, price, product)  # Insert into the left subtree.
        else:
            root.right = self.insert(root.right, price, product)  # Insert into the right subtree.

        # Update height of the current node after insertion.
        root.height = 1 + max(self._height(root.left), self._height(root.right))

        # Balance the tree and return the new root.
        return self._balance(root)

    def _height(self, node):
        """
        Retrieves the height of a given node.

        :param node: The node whose height is needed.
        :return: The height of the node, or 0 if the node is None.
        """
        return node.height if node else 0

    def _balance(self, node):
        """
        Balances the given node if it becomes unbalanced after insertion.
        
        :param node: The node to be balanced.
        :return: The balanced node.
        """
        if not node:
            return node

        # Update height
        node.height = 1 + max(self._height(node.left), self._height(node.right))
        
        # Get balance factor
        balance = self._get_balance(node)
        
        # Left Heavy
        if balance > 1:
            # Left-Right Case
            if self._get_balance(node.left) < 0:
                node.left = self._rotate_left(node.left)
            # Left-Left Case
            return self._rotate_right(node)
            
        # Right Heavy
        if balance < -1:
            # Right-Left Case
            if self._get_balance(node.right) > 0:
                node.right = self._rotate_right(node.right)
            # Right-Right Case
            return self._rotate_left(node)
            
        return node

    def _rotate_left(self, z):
        """Performs a left rotation"""
        y = z.right
        T2 = y.left
        
        y.left = z
        z.right = T2
        
        z.height = 1 + max(self._height(z.left), self._height(z.right))
        y.height = 1 + max(self._height(y.left), self._height(y.right))
        
        return y
        
    def _rotate_right(self, z):
        """Performs a right rotation"""
        y = z.left
        T3 = y.right
        
        y.right = z
        z.left = T3
        
        z.height = 1 + max(self._height(z.left), self._height(z.right))
        y.height = 1 + max(self._height(y.left), self._height(y.right))
        
        return y

    def is_balanced(self):
        """
        Checks if the entire tree is balanced according to AVL rules.
        Returns (is_balanced, height)
        """
        def check_balance(node):
            if not node:
                return True, 0
                
            left_balanced, left_height = check_balance(node.left)
            right_balanced, right_height = check_balance(node.right)
            
            # Check if both subtrees are balanced
            if not left_balanced or not right_balanced:
                return False, 0
                
            # Check balance factor
            balance = self._get_balance(node)
            is_balanced = abs(balance) <= 1
            
            height = 1 + max(left_height, right_height)
            
            return is_balanced, height
            
        balanced, _ = check_balance(self.root)
        return balanced

    def _get_balance(self, node):
        if not node:
            return 0
        return self._height(node.left) - self._height(node.right)

    def find_products_in_range(self, min_price, max_price):
        """
        Find all products within a given price range using in-order traversal.
        Returns a list of products with their names and prices.
        """
        result = []
        
        def inorder(node):
            if not node:
                return
                
            # If current node's price is greater than min_price,
            # then products in left subtree may be in range
            if node.price > min_price:
                inorder(node.left)
                
            # Check if current node is within range
            if min_price <= node.price <= max_price:
                result.append({
                    'name': node.product,
                    'price': node.price
                })
                
            # If current node's price is less than max_price,
            # then products in right subtree may be in range
            if node.price < max_price:
                inorder(node.right)
                
        inorder(self.root)
        return result
