from lindkedList import LinkedList




def findMid(ll):
    ptr = ll.head
    slow = ll.head
    fast = ll.head

    while fast.next is not None:
        fast = fast.next
        if fast.next is not None:
            fast = fast.next

        slow = slow.next


    return slow.ele

ll = LinkedList()
print(ll)
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)
ll.insert(5)
ll.insert(6)
ll.insert(7)
ll.print()

print("MID IS")
print(findMid(ll))