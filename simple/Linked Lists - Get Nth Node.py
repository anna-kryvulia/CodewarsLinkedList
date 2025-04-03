from node import Node

def get_nth(node, index):
    if node == None or index < 0:
        raise ValueError
    n = node
    for i in range(index):
        n = n.next
    if n == None:
        raise ValueError
    return n