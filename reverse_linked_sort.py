class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def reverse_print(x):
    stack = []
    current = x
    # while current:
    #     stack.append(current.data)
    #     current = current.next
    # while stack:
    #     print(stack.pop())

    while current:
        stack.append(str(current.data))
        current = current.next
    print("\n".join(stack[::-1]))

reverse_print(Node(3, Node(2, Node(1))))

'''second output method
# Initialize the linked list
head = Node(1)
node2 = Node(2)
head.next = node2
node3 = Node(3)
node2.next = node3

# Call the reverse_print function
reverse_print(head)
'''