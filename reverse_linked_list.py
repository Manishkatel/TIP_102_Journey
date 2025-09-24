#Reversing the linked list python
# OR I can call this a three pointer algorithm for remembering easily

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def printList(node):
    while node is not None:
        print(f"{node.data}", end="")
        if node.next is not None:
            print(" -> ", end="")
        node = node.next
    print()

def is_inversed(head):
    prev = None
    current = head
    while current:
        nxt = current.next      # save next
        current.next = prev     # reverse link
        prev = current          # move prev forward
        current = nxt           # move current forward
    return prev   # new head of reversed list
        
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head = is_inversed(head)
printList(head)
