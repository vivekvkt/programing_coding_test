

class Solutions:
    def find_Kth_smallest(self,arr,k):
        arr.sort()
        print("sorted",arr)

        return arr[k-1]


obj = Solutions()
arr= [12, 3, 5, 7, 19]
print(arr)
k=2
print(obj.find_Kth_smallest(arr,k))