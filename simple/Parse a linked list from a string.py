from node import Node

def linked_list_from_string(s):
    nodes = s.split(" -> ")[::-1]
    next = None
    if not nodes[1:]:
        return None
    for n in nodes[1:]:
        node = Node(int(n), next)
        next = node
    return node