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


