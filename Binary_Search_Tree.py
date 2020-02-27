'''
Binary search tree (BST) is a binary tree where the value of each node is larger or equal to the values in all the nodes in that node's left subtree and is smaller than the values in all the nodes in that node's right subtree.

Write a function that, efficiently with respect to time used, checks if a given binary search tree contains a given value.

For example, for the following tree:

n1 (Value: 1, Left: null, Right: null)
n2 (Value: 2, Left: n1, Right: n3)
n3 (Value: 3, Left: null, Right: null)

Call to contains(n2, 3) should return True since a tree with root at n2 contains number 3.
'''


import collections

Node = collections.namedtuple('Node', ['left', 'right', 'value'])


def contains(root, value):
    try:
        if root.value == value:
            return True
        if (root.value == None):
            return False
        if root.value < value:
            return contains(root.right, value)
        if root.value > value:
            return contains(root.left, value)
    except AttributeError:
        return False

n1 = Node(value=1, left=None, right=None)
n3 = Node(value=3, left=None, right=None)
n2 = Node(value=2, left=n1, right=n3)

print(contains(n2, 3))
