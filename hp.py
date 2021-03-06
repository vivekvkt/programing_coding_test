# lis = [
#     { "name" : "Nandini", "age" : 20}, 
#     { "name" : "Manjeet", "age" : 20 },
#     { "name" : "Nikhil" , "age" : 19 }
#     ]


# print(sorted(lis, key=lambda i: i['age'], reverse=True))

# def fingpattern(n):
#     k=1
#     for i in range(0,n):
#         for j in range(0,i+1):
#             print(k,end="")
#             if (j<i):
#                 print("*",end='')
#             k+=1
#         print()

#     k= k-n
#     temp = k
#     for i in range(n,-1,-1):
#         for j in range(1,i+1):
#             print(temp, end="")
#             if (i!=j):
#                 print("*",end="")
#                 temp+=1
                
#         print()
#         k-=(i-1)
#         temp=k


# fingpattern(4)


# numberGames= {}
# numberGames[(1,2,3)]=8
# numberGames[(4,2,3,5)]=10
# numberGames[(1,2)]=12

# #print(numberGames)

# s = 0

# for k in numberGames:
#     s+=numberGames[k]

# print(len(numberGames) +s )




# def  findArmstrong(n):
#     temp  = n
#     s = 0
#     while temp>0:

#         digit= temp%10
#         s += digit**3
#         temp = temp//10
        

#     if s==n:
#         print("armstrong")
#     else:
#         print("not arms")

# n = 153
# findArmstrong(n)

# def fibnaciseriese(n):

#     a,b=0,1
#     if n<0:
#         return n
#     elif n==0:
#         return a
#     elif n==1:
#         return b
#     else:

#         count =0
#         while count <=n:
#             nth = a+b
#             print(a)
#             a = b 
#             b = nth
#             count+=1
# n=9
# fibnaciseriese(n)



# def findSumOfPain(arr, sm,n):

    # s = set()

    # for i in range(0,n):
    #     temp = sm-arr[i]
    #     print(temp)
    #     if (temp in s):
    #         return ("(" + str(arr[i]) + "," + str(temp) + ")")
    #     s.add(arr[i])
    #     print("set",s)
   

# def reverseArray(arr,start,end):
#     data = arr[::-1]
#     print("data",data)
#     while start < end:
#         arr[start],arr[end]=arr[end],arr[start]
#         start+=1
#         end-=1


# arr = [1,2,3]
# start=0
# end= len(arr)-1
# reverseArray(arr,start,end)
# print(arr)

