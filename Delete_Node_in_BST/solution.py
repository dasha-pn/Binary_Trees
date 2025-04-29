"""Exercise 4"""

class TreeNode(object):
    """
    Node of a binary tree.

    Attributes:
        val (int): Value stored in the node.
        left (TreeNode): Left child.
        right (TreeNode): Right child.

    Example:
        >>> node = TreeNode(5)
        >>> node.val
        5
        >>> node.left is None
        True
        >>> node.right is None
        True
    """

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    """
    Provides a method to delete a node from a Binary Search Tree (BST).
    """

    def deleteNode(self, root: 'TreeNode', key: int) -> 'TreeNode':
        """
        Deletes the node with the given key from the BST.

        Args:
            root (TreeNode): The root of the BST.
            key (int): The value to delete.

        Returns:
            TreeNode: The new root of the BST after deletion.

        Example:
            >>> root = TreeNode(5, TreeNode(3), TreeNode(6))
            >>> sol = Solution()
            >>> new_root = sol.deleteNode(root, 3)
            >>> new_root.left is None
            True
        """

        if not root:
            return None

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            temp = self.find_max(root.left)
            root.val = temp.val
            root.left = self.deleteNode(root.left, temp.val)

        return root

    def find_max(self, node: 'TreeNode') -> 'TreeNode':
        """
        Finds the node with the maximum value in a BST.

        Args:
            node (TreeNode): The root of the subtree.

        Returns:
            TreeNode: The node with the maximum value.

        Example:
            >>> root = TreeNode(5, TreeNode(3), TreeNode(7))
            >>> sol = Solution()
            >>> max_node = sol.find_max(root)
            >>> max_node.val
            7
        """

        while node.right:
            node = node.right
        return node

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
