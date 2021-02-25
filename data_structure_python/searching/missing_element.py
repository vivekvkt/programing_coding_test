def findMissingElement(arr):
    n = len(arr)
    total_sum  = (n+1)*(n+2)//2
    #t = sum(arr)
    for i in range(n):
        total_sum-=arr[i]
    return total_sum

arr = [1, 2, 4, 5, 6]

print(findMissingElement(arr))

