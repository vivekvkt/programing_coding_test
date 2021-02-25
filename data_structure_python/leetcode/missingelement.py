

class Solution:
    def findMissingELement(self,arr):
        n = len(arr)
        total = (n+1)*(n+2)//2
        sum_of_total = sum(arr)
        return total - sum_of_total

    
obj = Solution()
arr = [1, 2, 4, 5, 6]
print(obj.findMissingELement(arr))