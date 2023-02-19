import io
import sys
from typing import List
# import pytest
from reverse_linked_sort import Node, reverse_print

def test_reverse_print():
    # Test 1: Empty linked list
    head = None
    captured_output = io.StringIO()
    sys.stdout = captured_output
    reverse_print(head)
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue() == ""

    # Test 2: Linked list with one node
    head = Node(1)
    captured_output = io.StringIO()
    sys.stdout = captured_output
    reverse_print(head)
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue() == "1\n"

    # Test 3: Linked list with multiple nodes
    head = Node(1)
    node2 = Node(2)
    head.next = node2
    node3 = Node(3)
    node2.next = node3
    captured_output = io.StringIO()
    sys.stdout = captured_output
    reverse_print(head)
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue() == "3\n2\n1\n"
