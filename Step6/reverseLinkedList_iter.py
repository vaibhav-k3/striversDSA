from lindkedList import LinkedList


def reverse_list(ll):
    curr = ll.head
    next = None
    prev = None
    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    ll.head = prev







ll = LinkedList()
ll.print()
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)
ll.insert(5)
ll.insert(6)
ll.insert(7)
ll.print()
print()
reverse_list(ll)
ll.print()