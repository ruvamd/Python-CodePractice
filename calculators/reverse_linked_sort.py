class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def reverse_print(l):
    if l is None:
        return
    reverse_print(l.next)
    print(l.data)

# Example usage
head = Node(1, Node(2, Node(3)))
reverse_print(head)
# Output:
# 3
# 2
# 1
