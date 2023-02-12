from lib2to3.pytree import Node


def reverse(x: Node) -> Node:
    prev = None
    current = x
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

def print_linked_list(head: Node):
    current = head
    while current:
        print(current.data)
        current = current.next
x=
head = reverse()
print_linked_list(head)
