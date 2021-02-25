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
