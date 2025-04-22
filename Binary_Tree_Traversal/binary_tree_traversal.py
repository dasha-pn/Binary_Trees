"""Different traversals of the binary tree (exercise 1)"""

class Node:
    """
    A class representing a node in a binary tree.
    
    Attributes:
        name: The value or name of the node.
        left: Reference to the left child node.
        right: Reference to the right child node.
    """

    def __init__(self, data, left=None, right=None):
        self.name = data
        self.left = left
        self.right = right

# Pre-order traversal
def pre_order(node):
    """
    Traverse the binary tree in pre-order: root → left → right.

    Args:
        node (Node): The root of the binary tree.

    Returns:
        list: A list of node values (data) in pre-order traversal.

    >>> a = Node(1, Node(2), Node(3))
    >>> pre_order(a)
    [1, 2, 3]
    """

    if not node:
        return []
    return [node.data] + pre_order(node.left) + pre_order(node.right)


# In-order traversal
def in_order(node):
    """
    Traverse the binary tree in in-order: left → root → right.

    Args:
        node (Node): The root of the binary tree.

    Returns:
        list: A list of node values (data) in in-order traversal.

    >>> a = Node(1, Node(2), Node(3))
    >>> in_order(a)
    [2, 1, 3]
    """

    if not node:
        return []
    return in_order(node.left) + [node.data] + in_order(node.right)


# Post-order traversal
def post_order(node):
    """
    Traverse the binary tree in post-order: left → right → root.

    Args:
        node (Node): The root of the binary tree.

    Returns:
        list: A list of node values (data) in post-order traversal.

    >>> a = Node(1, Node(2), Node(3))
    >>> post_order(a)
    [2, 3, 1]
    """

    if not node:
        return []
    return post_order(node.left) + post_order(node.right) + [node.data]

if __name__ == "__main__":
    a = Node("A")
    b = Node("B")
    c = Node("C")
    a.left = b
    a.right = c

    print("Pre-order:", pre_order(a))
    print("In-order:", in_order(a))
    print("Post-order:", post_order(a))

    import doctest
    doctest.testmod(verbose=True)
