# product - price, name, customer_id
# customer - name, address, contact


# class Product(models.Model):
#     name = models.CharFiled(max_length=200)

#     price  = models.IntergerField()
#     customer_id = models.ManytoMany()



# class Customer(models.Model):
#     name = models.CharFiled()
#     address = models.CharFiled()
#     contact = models.CharFiled()
#     product = models.ForeignKey(Product)



# serielizer===


# class CustomerSerializers(serielizer.ModelSerializer):

#     class Meta:
#         model = Customer
#         fields = "__all_"  

# [default]
# aws_access_key_id="AWS_id"
# aws_secret_access_key="AWS secret" 

# {
# "data":
# {
# "aws_access":"dsdsds",
# "aws_secret":"secret"
# }

# }
#    {%  for item in data %}
#     {{ data['aws_access']}}

#     {{ data['aws_secret']  }}

#     {% endIf %}


# employee_table- name, exp, expeiece, manager_id

# select *from employee_table where manager_id=2

# def findPalindrom(stri):

#     return  stri == stri[::-1] 

# stri="radar"
# print(findPalindrom(stri))







    
