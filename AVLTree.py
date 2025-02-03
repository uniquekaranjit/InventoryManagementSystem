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
        balance_factor = self._height(node.left) - self._height(node.right)  # Calculate balance factor.

        # Placeholder: Actual balancing logic (rotations) should be implemented here.

        return node  # Currently returns the node without balancing (needs implementation).
