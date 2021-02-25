lst  = [1,2,3,4]

myiter = iter(lst)

# print(next(myiter))
# print(next(myiter))
# print(next(myiter))



while True:
    try:
        element = next(myiter)
        print(element)

    except StopIteration:
        break
