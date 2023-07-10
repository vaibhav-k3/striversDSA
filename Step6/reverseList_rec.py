from lindkedList import LinkedList
from lindkedList import Node



def reverse_list(node):
    if node is None or node.next is none:
        return node
    
    node1 = reverse_list(node.next)
    node.next.next = node
    node.next = None
    return node1

ll = LinkedList()
ll.print()
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)
ll.insert(5)
ll.insert(6)
ll.insert(7)

