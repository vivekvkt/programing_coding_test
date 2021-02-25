# class Solution:
#     def findRepeatedElement(self,arr):
#         n = len(arr)
#         repeated = []
#         for i in range(n):
#             k = i+1
#             for j in range(k,n):
#                 if arr[i]==arr[j] and arr[i] not in repeated:
#                     repeated.append(arr[i])
#         return repeated


# obj = Solution()
# arr = [-1, 1, -1, 8]
# print(obj.findRepeatedElement(arr))


def printRepeating(arr, size):
    for i in range(0, size):
 
        if arr[abs(arr[i])] >= 0:
            arr[abs(arr[i])] = -arr[abs(arr[i])]
        else:
            print(abs(arr[i]), end=" ")
 
 
# Driver code
arr = [1, 2, 3, 1, 3, 6, 6]
arr_size = len(arr)
 
printRepeating(arr, arr_size)