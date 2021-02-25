# class Node:
#     def __init__(self, data):
#         self.left = None
#         self.right = None
#         self.data  = data


#     def preOrderTree(self):
#         print(self.data)
#         if self.left:
#             self.left.preOrderTree()
#         if self.right:
#             self.right.preOrderTree()

#     def inOrderTree(self):
#         if self.left:
#             self.left.inOrderTree()
#         print(self.data)
#         if self.right:
#             self.right.inOrderTree()
    

#     def postOrder(self):
#         if self.left:
#             self.left.postOrder()
#         if self.right:
#             self.right.postOrder()
#         print(self.data)
# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)

# print("preorder data... ")
# root.preOrderTree()
# print("inorder data treee... ")
# root.inOrderTree()
# print("post Order data ... ")

# root.postOrder()
# print()


# class BinaryTree:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

#     def display(self):
#         print(self.data)
#         print(self.left.data)
#         print(self.right.data)

# root = BinaryTree(1)
# root.left = BinaryTree(2)
# root.right = BinaryTree(3)
# root.display()
