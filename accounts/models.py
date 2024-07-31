
# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

ROLE_CHOICES = (
    ("1" , "Patient"),
    ("2" , "Doctor"),

)
GENDER_CHOICES = (
    ("M" , "MALE"),
    ("F" , "FEMALE"),
    ("O" , "OTHER"),
) 

class User(AbstractUser):
    phone_number = models.BigIntegerField(null=True, blank=True)
    role = models.CharField(max_length = 20,choices = ROLE_CHOICES,default = '1')
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length = 7, choices = GENDER_CHOICES,default = '1')
    Year_of_experience = models.IntegerField(null=True,blank=True)
    date_of_birth = models.DateTimeField(null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    Specialization = models.CharField(max_length=50,null=True, blank=True)
    image = models.ImageField(upload_to='profile_images/', default='default_profile_image.png')

    def __str__(self):
        return self.user.username