# def dec(fun):
#     def inner():
#         print("hello dec")
#         fun()
#     return inner


# @dec
# def ordinary():
#     print("hello ordinary")

# ordinary()

# dom = dec(ordinary)
# dom()

# def sumNo(*num):
#     s = 0

#     for i in num:
#         s = s + i

#     print(s)

# sumNo(10,20,50)


# def intro(**data):
    
#     for key,value in data.items():
#         print(key, value)

# intro(firstname="vivek",lastname="tiwari",vill="noida")

# data = lambda x : x **2
# print(data(2))

lst = [10,3,2,40,60,70,80]
# lst.extend([100])
# print(lst)

 
new_list = list(filter(lambda x :(x%2==0),lst))
print("length",len(new_list))
print(new_list)


