from node import Node

class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    if head == None or head.next == None:
        raise ValueError
        
    n1 = Node()
    n2 = Node()
    l1 = n1
    l2 = n2
    i = True
    
    current = head
    while current:
        next_node = current.next
        current.next = None

        if i:
            l1.next = current
            l1 = l1.next
        else:
            l2.next = current
            l2 = l2.next

        i = not i
        current = next_node

    return Context(n1.next, n2.next)