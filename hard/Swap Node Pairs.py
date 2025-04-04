from node import Node

def swap_pairs(head):
    n = Node(0)
    n.next = head
    prev = n

    while head and head.next:
        first = head
        second = head.next

        prev.next = second
        first.next = second.next
        second.next = first

        prev = first
        head = first.next

    return n.next