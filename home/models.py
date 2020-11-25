from djongo import models
from django.utils import timezone
from django.core.validators import RegexValidator
import re
# Create your models here.


class Post(models.Model):
    auther = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    pub_date = models.DateTimeField(default = timezone.now)
    mainphoto = models.ImageField(blank=True, null=True) #

    def __str__(self):
        return self.title

class Support(models.Model):
    name = models.CharField(max_length=50)

    phone_regex = RegexValidator(regex=r'\d{2,3}-\d{3,4}-\d{4}', message="")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) 

    email_regex = RegexValidator(regex=r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}', message="") 
    email = models.CharField(validators=[email_regex], max_length=200, blank=True) 

    contents = models.TextField(blank=True)

    def __str__(self):
        return self.name