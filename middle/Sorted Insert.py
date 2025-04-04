from node import Node

def sorted_insert(head, data):
    n = Node(data)
    
    if head is None or data < head.data:
        n.next = head
        return n

    current = head
    while current.next is not None and current.next.data < data:
        current = current.next

    n.next = current.next
    current.next = n
    return head