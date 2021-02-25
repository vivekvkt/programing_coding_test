# a=[1,3,45,56,4,11.23]

# a.sort()
# print(a)

# a=[1,2,3,4,5,6,7]  # output [4,5,6,7,1,2,3]  3 rotation

# def findRotation(a):
#     n= len(a)

# delete  from table  where  id/name = somthing

# update table  set = 'something' where id = something

# select  e.name , b.sal from emp as e inner join b on e.id = b.id 



# def leftRotate(arr, d, n):
#     for i in range(d):
#         leftRotateOne(arr,n)

# def leftRotateOne(arr, n):
#     temp= arr[0]
#     for  i in range(n-1):
#         arr[i] = arr[i+1]
#     arr[n-1] =  temp


# def printArray(arr, size):
#     for i in range(size):
#         print(arr[i])

# arr = [1, 2, 3, 4, 5, 6, 7] 
# n = len(arr)
# leftRotate(arr, 3, n) 
# printArray(arr, n)



# def printPairs(arr, n, sum):
#     s = set()

#     for i in range(0,n):
#         temp = sum-arr[i]
#         if temp in s:
#             print( str(arr[i]) , str(temp))
#         else:
#             s.add(arr[i])



# A = [1, 4, 45, 6, 10, 8]
# n = 16
# printPairs(A, len(A), n)


# def findPairElement(arr,sum):
#     n = len(arr)-1
#     count = 0

#     for i in range(0,n):
#         j = i+1
#         if (arr[i] + arr[j]==sum):
#             print( arr[i], arr[j])
#             count +=1
#     return count
 
# #arr =[10, 12, 10, 15, -1, 7, 6,5, 4, 2, 1, 1, 1]
# arr = [1, 5, 7, -1]
# #sum = 11
# sum = 6

# print(findPairElement(arr, sum))
