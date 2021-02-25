def findLinearSearch(arr, n, x):
    
    for i in range(0,n):
        
        if (arr[i]==x):
            return i
    return -1


arr = [2, 3, 4, 10, 40]
n = len(arr)
x = 10
print(findLinearSearch(arr, n,x))