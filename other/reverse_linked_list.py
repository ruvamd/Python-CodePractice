class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def reverse(x):
    prev = None
    curr = x
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev

# Create linked list 1 -> 2 -> 3
head = Node(1, Node(2, Node(3)))

# Reverse the linked list
reversed_head = reverse(head)

# Print the reversed linked list
curr = reversed_head
while curr:
    if curr.next:
        print(curr.val, end=' -> ')
    else:
        print(curr.val)
    curr = curr.next

# Output:
# 3 -> 2 -> 1
