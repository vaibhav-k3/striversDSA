class Node:
    def __init__(self,ele):
        self.next = None
        self.ele = ele


class LinkedList:
    def __init__(self):
        self.head = None
        

    def insert(self,ele):
        if self.head is None:
            self.head = Node(ele)
            return self
        else:
            ptr = self.head
            while ptr.next is not None:
                ptr = ptr.next
            ptr.next = Node(ele)

    def print(self):
        ptr = self.head
        while ptr is not None:
            print(ptr.ele,end="->")
            ptr=ptr.next

