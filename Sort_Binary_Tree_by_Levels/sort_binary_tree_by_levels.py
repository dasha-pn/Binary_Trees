"""Sort binary tree by levels"""

from collections import deque

class Node:
    """."""

    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n

def tree_by_levels(node: Node):
    """
    >>> tree_by_levels(None) is None
    True
    >>> tree_by_levels(Node(Node(None, Node(None, None, 4), 2), \
Node(Node(None, None, 5), Node(None, None, 6), 3), 1))
    [1, 2, 3, 4, 5, 6]
    """

    if not node:
        return None

    queue = deque([node])
    res = []

    while queue:
        cur = queue.popleft()
        res.append(cur.value)

        if cur.left:
            queue.append(cur.left)
        if cur.right:
            queue.append(cur.right)

    return res

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
