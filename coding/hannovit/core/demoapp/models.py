from django.db import models



class Patient(models.Model):
    SEX_CHOICES = (
    ('female', 'female',),
    ('male', 'male',)
    
    )
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    gender = models.CharField(max_length=10,choices=SEX_CHOICES,)
    dob = models.DateField(max_length=20)


    def __str__(self):
        return self.firstname
