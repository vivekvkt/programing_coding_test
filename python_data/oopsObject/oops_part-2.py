# class P:
#     def m1(self):
#         print("hello vviek")
# class C(P):
#     def m2(self):
#         print("not vivek")




# c = C()
# c.m1()
# c.m2()


class P:
    a = 100
    def __init__(self):
        self.b = 30
        print("data")

class C(P):
    def __init__(self):
        print("hello vivek")
        super().__init__()


d = C()
print(d.a)
print(d.b)