class Tree:
    def __init__(self, values):
        self.root = None
        if values:
            for value in values:
                self.insert(value)

    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_node(self.root, value)

    def _insert_node(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_node(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_node(node.right, value)

    def in_order(self):
        return self._in_order_traversal(self.root)

    def _in_order_traversal(self, node):
        if node is None:
            return ''
        else:
            return (self._in_order_traversal(node.left) +
                    str(node.value) + ' ' +
                    self._in_order_traversal(node.right))

    def pre_order(self):
        return self._pre_order_traversal(self.root)

    def _pre_order_traversal(self, node):
        if node is None:
            return ''
        else:
            return (str(node.value) + ' ' +
                    self._pre_order_traversal(node.left) +
                    self._pre_order_traversal(node.right))

    def post_order(self):
        return self._post_order_traversal(self.root)

    def _post_order_traversal(self, node):
        if node is None:
            return ''
        else:
            return (self._post_order_traversal(node.left) +
                    self._post_order_traversal(node.right) +
                    str(node.value) + ' ')

    def height(self):
        return self._get_height(self.root)

    def _get_height(self, node):
        if node is None:
            return 0
        else:
            left_height = self._get_height(node.left)
            right_height = self._get_height(node.right)
            return max(left_height, right_height) + 1

    def sum(self):
        return self._get_sum(self.root)

    def _get_sum(self, node):
        if node is None:
            return 0
        else:
            return node.value + self._get_sum(node.left) + self._get_sum(node.right)

    def contains(self, value):
        return self._contains_value(self.root, value)

    def _contains_value(self, node, value):
        if node is None:
            return False
        elif node.value == value:
            return True
        elif value < node.value:
            return self._contains_value(node.left, value)
        else:
            return self._contains_value(node.right, value)

    def delete(self, value):
        if not self.root:
            return self.root
        
        def find_min(node):
            while node.left:
                node = node.left
            return node

        def delete_helper(node, value):
            if not node:
                return node

            if value < node.value:
                node.left = delete_helper(node.left, value)
            elif value > node.value:
                node.right = delete_helper(node.right, value)
            else:
                if not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                else:
                    temp = find_min(node.right)
                    node.value = temp.value
                    node.right = delete_helper(node.right, temp.value)
            return node

        self.root = delete_helper(self.root, value)

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# create a new binary search tree with the values [10, 15, 7, 9, 3, 24, 36]
tree = Tree([10, 15, 7, 9, 3, 24, 36])

# print the in-order traversal of the tree
print(tree.in_order())  # output: 3 7 9 10 15 24 36

# print the pre-order traversal of the tree
print(tree.pre_order())  # output: 10 7 3 9 15 24 36 

# print the post-order traversal of the tree
print(tree.post_order())  # output: 3 9 7 36 24 15 10

# get the height of the tree
print(tree.height())  # output: 4

# get the sum of all values in the tree
print(tree.sum())  # output: 104

# check if the value 4 exists in the tree
print(tree.contains(4))  # output: False

# check if the value 10 exists in the tree
print(tree.contains(10))  # output: True


tree.delete(9)
print(tree.in_order())  # Output: 3 7 10 15 24 36

#flipped tree
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def flip_tree(root):
    if root is None:
        return None
    
    # swap the left and right children of the current node
    root.left, root.right = root.right, root.left
    
    # recursively flip the left and right subtrees
    flip_tree(root.left)
    flip_tree(root.right)
    
    return root

# create the original tree
root = Node(4)
root.left = Node(2, Node(1), Node(3))
root.right = Node(7, Node(6), Node(9))

# print the original tree
def print_tree(root):
    if root is None:
        return
    print(root.val)
    print_tree(root.left)
    print_tree(root.right)

print("Original tree:")
print_tree(root)

# flip the tree
flipped = flip_tree(root)

# print the flipped tree
print("Flipped tree:")
print_tree(flipped)
