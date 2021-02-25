class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


    
class LinkedList:
    def __init__(self):
        self.head = None


    
    def push_data(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next


    def detectLoop(self):
        slow_ptr = self.head
        fast_ptr = self.head
        while(slow_ptr  and fast_ptr and fast_ptr.next):
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
            if slow_ptr==fast_ptr:

                return
            


listdata = LinkedList()
listdata.push_data(1)
listdata.push_data(2)
listdata.push_data(3)
listdata.push_data(4)
#listdata.push_data(5)
#listdata.printList()
listdata.head.next.next.next.next = listdata.head
if (listdata.detectLoop()):
    print("found loop")
else:
    print("not found loop")