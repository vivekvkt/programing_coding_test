# l1= [1,2,3,5,8]
# l2 = [1,2,3,6,3]

# n1 = sorted(l1)
# n2 = sorted(l2)
# x1= len(n1)

# for i in range(0, x1):
#     if n1[i]!=n2[i]:
#         print(n1[i], n2[i])
    


# def findFibonaci(num):
#     a,b = 0,1
#     if num<0:
#         print("valid no")
#     elif num ==1:
#         print(num)
#     else:
#         i=0
#         while i<=num:
#             print(a)
#             nth = a+b
#             a=b
#             b= nth
#             i+=1
# num = 9
# findFibonaci(num)


# def findFibNum(num):
#     if num<=1:
#         return num
#     else:
#         return findFibNum(num-1) + findFibNum(num-2)

# num = 10

# if num<=0:
#     print("valid number")

# else:
#     for i in range(num):
#         print(findFibNum(i))


# def reverseNumber(num):
#     temp = num
#     rev = 0
#     while temp >0:
#         lastdigit = temp % 10
#         rev  = (rev*10) + lastdigit
#         temp  = temp //10
#     return rev

# n = 12345678910
# print(reverseNumber(n))


# str = "geeksforgeeks"  # segoseg
# res = str[-1:-14:-2]
# print(res)

# a = {'a':10,'b':20}
# b = {'a':130, 'd':400}

# d  = {**a,**b}
# print(d)


# class PrintString:
#     def __init__(self, s):
#         self.s = s

    

#     def __add__(self, other):
#         return self.s  + other


#     def __str__(self):
#         return  self.s

# if __name__ == "__main__":
#     str1 = PrintString('hello')
#     print(str1 + " vivek ")

# name = "vivek hello"
# print(list(name.split(" ")))


# l1 = ["vivek","eat","data"]

# for i in enumerate(l1,30):
#     print(i)


# class A:
#     def rk(self):
#         print("class A")

# class B(A):
#     def rk(self):
#         print("class B")
#         #super().rk()

# class C(A):
#     def rk (self):
#         print("class C")

# class D(C,B):
#     pass
#     # def rk(self):
#     #     print("class D")


# r = D()
# r.rk()

# print(D.__mro__)
# print(D.mro())

# import copy
# a = ['a',1,2,'d']

# b = a
# # b[0]=10
# # print(id(b))
# # print(id(a))

# d = [1,2,3,[4,5,6],10]
# # e = copy.copy(d)
# e = copy.deepcopy(d)
# e[0]=200
# e[3][0]=100

# print(d)
# print(e)




# def reverseStrArrayWithoutTemp(str,start,end):
#     while(start<end):

#         str =   (str[:start]+ chr(ord(str[start]) ^ ord(str[end])) + str[start+1:])

#         str =  ( str[:end]+ chr(ord(str[start]) ^ ord(str[end])) + str[end+1:])
#         str =   (str[:start]+ chr(ord(str[start]) ^ ord(str[end])) + str[start+1:])

#         start+=1
#         end-=1

#     return str


# s =  "abc"
# start=0
# end = len(s)-1
# print(reverseStrArrayWithoutTemp(s,start,end))





class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


    def reverseLinkedList(self):
        prev = None
        current = self.head
        while(current):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def pushData(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def print_data(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next




node = LinkedList()
node.pushData(10)

node.pushData(20)
node.pushData(30)
# node.pushData(40)

# #node.print_data()

# node.reverseLinkedList()
# node.print_data()


def findSumOfNUm(arr, n,s):
    st = set()

    for i in range(0, n):
        temp = s- arr[i]
        print("temp",temp)
        if (temp in st):
            print( "(",str(arr[i])+", "+str(temp),")")
        st.add(arr[i])
    print("set",st)

# A = [1, 4, 45, 6, 10, 8]
# s = 16
A= [0, -1, 2, -3, 1]
s= -2 
findSumOfNUm(A, len(A), s)
