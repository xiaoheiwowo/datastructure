class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


binary_tree = Node('A', Node('B', Node('D', Node('H')), Node('E')), Node(
    'C', Node('F'), Node('G', Node('I', right=Node('J')))))


def level_traverse(tree):
    queue = []
    queue.append(tree)
    while len(queue) > 0:
        n = queue.pop(0)
        if n.val is not None:
            print(n.val)
        if n.left is not None:
            queue.append(n.left)
        if n.right is not None:
            queue.append(n.right)


def pre_traverse(tree):
    if tree is not None:
        print(tree.val)
        pre_traverse(tree.left)
        pre_traverse(tree.right)


def mid_traverse(tree):
    if tree is not None:
        pre_traverse(tree.left)
        print(tree.val)
        pre_traverse(tree.right)


def after_traverse(tree):
    if tree is not None:
        pre_traverse(tree.left)
        pre_traverse(tree.right)
        print(tree.val)


pre_traverse(binary_tree)
print('========================')
mid_traverse(binary_tree)
print('========================')
after_traverse(binary_tree)
print('========================')
level_traverse(binary_tree)