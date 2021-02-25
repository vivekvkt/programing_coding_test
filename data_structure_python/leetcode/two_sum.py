
# def two_sum(arr, target):
#     list_data = []
#     n = len(arr)-1
#     for i in  range(n):
#         j = i+1
#         if (arr[i]+arr[j]==target):
#             list_data.append(i)
#             list_data.append(j)
#     return list_data


# arr = [3,2,4]#[2,7,11,15]
# target = 6 #target = 9
# # Input: nums = [3,2,4], target = 6
# # Output: [1,2]

# print(two_sum(arr,target))

# class Solution:
#     def twoSum(self, nums, target: int):
#         List =[]
#         n = len(nums)-1
#         for i in range(n):
#             j = i+1
#             if (nums[i]+nums[j]==target):
#                 List.append(i)
#                 List.append(j)
#         return List
    
# #Runtime: 20 ms
  
# solve = Solution()
# nums = [3,2,3]#[2,7,11,15] 
# target = 6 #9
# print(solve.twoSum(nums,target))
        

def twoSum(nums, target):
    output=[]
    arr=sorted(nums)
    x=0
    y=-1
    X=len(nums)-1
    while x<X:
        if (arr[X]+arr[x] >  target):
            X-=1 
        elif (arr[X]+arr[x] <  target):
            x+=1
        elif (arr[X]+arr[x] == target):
            #print("Found",arr[X],arr[x])
            num1=arr[x]
            num2=arr[X]
            x+=1
            X-=1 
    for i in range(len(nums)):
        if num1 == nums[i] and y==-1:
            index1=i
            y=i
        elif num2 == nums[i]:
            index2=i         
    return [index1, index2]

nums = [3,2,3]#[2,7,11,15] 
target = 6 #9
print(twoSum(nums,target))