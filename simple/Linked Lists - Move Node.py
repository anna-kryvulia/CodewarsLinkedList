from node import Node

class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest
    
def move_node(source, dest):
    if not source:
        raise ValueError
    n = Node(source.data)
    n.next = dest
    return Context(source.next, n)