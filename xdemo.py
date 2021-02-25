
# lst = [1,2,3,4]

# data = list(map(lambda x:x*2,lst))

# print(data)

# car= Vehicle.new.maker("honda").model("civic")
# print(car.maker) # honda
# print(car.model) # civic


# class Vehicle:

#     def __init__(self, maker, model):
#         self.maker = maker
#         self.model = model


#     def maker(self,):
#         return self.maker

#     def model(self):
#         return self.model

    
# car = Vehicle("honda","civic")
# print(car.maker)
# print(car.model)

# Input:   str = "a,b$c"
# Output:  str = "c,b$a"
# Note that $ and , are not moved anywhere.  
# Only subsequence "abc" is reversed

# Query to Get all user with comments count

# TABLES
# USER(ID,NAME)
# COMMENT(ID,COMMENT,USER_ID)


# User.objects.select_related('COMMENT').all().count()
# User.objects.annotate(count=Count('comment')).all().
# User.objects.all().annotate(total_comment=Count('comment'))

# what is difference between merge and rebase in git
# how using pull in git






