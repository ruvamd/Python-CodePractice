class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self, values):
        self.root = None
        for value in values:
            self.insert(value)
            
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            current_node = self.root
            while True:
                if value < current_node.value:
                    if current_node.left is None:
                        current_node.left = Node(value)
                        break
                    else:
                        current_node = current_node.left
                elif value > current_node.value:
                    if current_node.right is None:
                        current_node.right = Node(value)
                        break
                    else:
                        current_node = current_node.right
                else:
                    break
    
    def in_order(self):
        result = []
        self._in_order_traversal(self.root, result)
        return ' '.join(map(str, result))

    def _in_order_traversal(self, node, result):
        if node is not None:
            self._in_order_traversal(node.left, result)
            result.append(node.value)
            self._in_order_traversal(node.right, result)

    def pre_order(self):
        result = []
        self._pre_order_traversal(self.root, result)
        return ' '.join(map(str, result))

    def _pre_order_traversal(self, node, result):
        if node is not None:
            result.append(node.value)
            self._pre_order_traversal(node.left, result)
            self._pre_order_traversal(node.right, result)

    def post_order(self):
        result = []
        self._post_order_traversal(self.root, result)
        return ' '.join(map(str, result))

    def _post_order_traversal(self, node, result):
        if node is not None:
            self._post_order_traversal(node.left, result)
            self._post_order_traversal(node.right, result)
            result.append(node.value)

    def height(self):
        return self._get_height(self.root)

    def _get_height(self, node):
        if node is None:
            return -1
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
        return self._contains_helper(self.root, value)
    
    def _contains_helper(self, node, value):
        if node is None:
            return False
        elif node.value == value:
            return True
        elif value < node.value:
            return self._contains_helper(node.left, value)
        else:
            return self._contains_helper(node.right, value)
        
