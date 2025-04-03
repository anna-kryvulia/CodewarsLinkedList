from node import Node

def stringify(node):
    '''returns node in str form'''
    s = ''
    head = node
    while head != None:
        s += str(head.data) + " -> "
        head = head.next

    return s + 'None'
