
"""find missing element in array"""
# def findMissingELement(arr):
#     n = len(arr)
#     total_sum = (n+1)*(n+2)//2

#     for i in range(n):
#         total_sum = total_sum - arr[i]

#     return total_sum

# arr = [1, 2, 4, 6, 3, 7, 8]
# print(findMissingELement(arr))

""" find duplicates in array"""


# def  duplicateArray(arr):
#     repeated = []
#     n = len(arr)
#     for i in range(n):
#         k = i + 1
#         for j in range(k, n):
#             if arr[i]==arr[j] and arr[i] not in repeated:
#                 repeated.append(arr[i])
#     return repeated

# arr = [10, 20, 30, 20, 20, 30, 40,50, -20, 60, 60, -20, -20] 

# print(duplicateArray(arr))



""" find pair of sum === sum"""

# def findPairOfSum(arr,sum_data):
#     print(sum_data)
#     low = 0
#     high = len(arr)-1
#     while low < high:
#         if (arr[low] + arr[high]==sum_data):
#             # print(" sum value :(",arr[low],',',arr[high],") ")
#             print("The pair is : (", arr[low],", ", arr[high], ")")
#         if (arr[low]+arr[high]> sum_data):
#             high-=1
#         else:
#             low+=1


# arr = [2, 3, 4, -2,6, 8, 9, 11]
# arr.sort()
# sum_data=6
# findPairOfSum(arr,sum_data)


""" remove duplicate from array """




# def removeDuplicate(arr):
#     list_data = []
#     for item in arr:
#         if item not in  list_data:
#             list_data.append(item)
#     return list_data



arr = [1, 2, 2, 3, 4, 4, 4, 5, 5] 
# print(removeDuplicate(arr))

# arr = [1, 2, 2, 3, 4, 4, 4, 5, 5] 
# list_data = []
# data = [list_data.append(item) for item in arr if item not in list_data]
# print(list_data)

#data = arr[::-1]
#arr.reverse()

# def revrseArray(arr):
#     start=0
#     end = len(arr)-1
#     while start < end:
#         arr[start],arr[end]= arr[end],arr[start]
#         start+=1
#         end-=1
    
# arr = [1, 2, 3, 4, 5, 6]

# revrseArray(arr)
# print(arr)





# x = ['ab','cd']

# for i in x:
#     x.append(i.upper())

# print(x)

class Solution:
    def findProductExceptSelf(self,arr):
        output=[1]
        for i in range(len(arr)-1,0,-1):
            output.append(output[-1]*arr[i])
        output=output[::-1]
        left = 1
        for i in range(len(arr)):
            output[i]= output[i]*left
            left*=arr[i]
        return output

obj = Solution()
arr = [1,2,3,4,5]
print(obj.findProductExceptSelf(arr))












