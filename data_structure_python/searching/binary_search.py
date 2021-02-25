def binarySearch(arr, l, r, skey):
    
    if l<=r:

        mid = l+(r-1)//2
       
        if (arr[mid]==skey):
            return mid
        elif arr[mid]>skey: 
           
            return binarySearch(arr,l, mid-1,skey)
        else:
            return binarySearch(arr, mid+1, r, skey)
        
    else:
        return -1  

arr = [ 2, 3, 4, 10, 40 ] 
skey = 10
print(binarySearch(arr,0, len(arr)-1, skey))

        