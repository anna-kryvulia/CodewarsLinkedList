from node import Node

def push(head, data):
    n = Node(data)
    n.next = head
    return n

def build_one_two_three():
    chained = None
    chained = push(chained, 3)
    chained = push(chained, 2)
    chained = push(chained, 1)
    return chained