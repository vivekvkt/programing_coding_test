class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LikedListDemo:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node


    def afterNode(self, preveNode, new_data):
        if preveNode is None:
            print("previous node must be linkedlist")
            return
        new_node = Node(new_data)

        new_node.next = preveNode.next
        preveNode.next  = new_node

    def appendNode(self, new_data):
        new_node = Node(new_data)
        if self.head is  None:
            self.head = new_node
            return

        last = self.head
        while(last.next):
            last = last.next
        last.next = new_node

    def deleteNode(self, key):
        temp = self.head
        if (temp is not None):
            if(temp.data ==key):
                self.head = temp.data
                temp = None
                return

        while(temp is not None):
            



    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next


node  = LikedListDemo()
# node.head = Node(1)
# second = Node(2)
# third = Node(3)
# node.head.next = second
# second.next = third

node.push(30)
node.push(40)
node.push(100)
node.afterNode(node.head.next,505)
node.afterNode(node.head.next.next,400)
node.appendNode(50)
node.deleteNode(1)

node.printList()
