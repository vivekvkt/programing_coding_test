#segregate even and odd 

def SegregrateEvenAndOdd(arr):
    left ,right = 0,len(arr)-1
    n = len(arr)-1
    while left < right:
        while (arr[left]%2==0 and left < right):
            #print("lft",arr[left])
            left+=1
        while (arr[right]%2==1 and left < right):
            #print("right",arr[right])
            right-=1
        while left < right:
            arr[left],arr[right] = arr[right],arr[left]
            left+=1
            right-=1
           
            
arr = [12, 34, 45, 9, 8, 90, 3]
SegregrateEvenAndOdd(arr)
# for i in range(0, len(arr)):
#     print(arr[i])


def segEvenOdd(arr,n):
    j = -1
    for i in range(0,n):
        if arr[i]%2==0:
            j+=1
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp

arr = [10,3,20,5,40,43,7]
n = len(arr)
segEvenOdd(arr,n)

# for i in range(0,n):
#     print(arr[i])

# def segregate0and1(arr):
#     # a1=[]
#     # a2=[]
#     # for i in range(len(arr)):
#     #     if arr[i]==0:
#     #         a1.append(arr[i])
#     #     if arr[i]==1:
#     #         a2.append(arr[i])
#     # datalist = a1+a2
#     # print(datalist)
#     datalist = ([x for x in arr if x==0] +[x for x in arr if x==1])
#     #print(datalist)

# arr=[0, 1, 0, 1, 0, 0, 1, 1, 1, 0]
# segregate0and1(arr)


import numpy as np
import pandas as pd

# arr  = np.array([[6,7,8],[1,2,3],[9,3,2]])
# print(arr[-1,0:2])

arr  = np.array([[1,2],[3,4],[5,6]])
a = (1,2,3,4,5,6)
print(a[-3])


