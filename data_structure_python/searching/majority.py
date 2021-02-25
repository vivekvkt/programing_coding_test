def findMajorityElement(arr):

    m = {}
    n = len(arr)
    for i in range(n):
        if arr[i] in m:
            m[arr[i]]+=1
        else:
            m[arr[i]]=1

    count = 0
    for key in m:
        if m[key]> n/2:
            count=1
            print('find majority element-',key)
            break
        if count==0:
            print("no majority element")

# Driver code 
arr = [2, 2, 2, 2, 5, 5, 2, 3, 3]  
# Function calling 
findMajorityElement(arr)