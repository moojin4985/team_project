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
    idx = models.AutoField(primary_key=True)
    auther = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=False)

    phone_regex = RegexValidator(regex=r"^[0-9]{3}-[0-9]{3,4}-[0-9]{4}$", message="")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) 
    
    email = models.EmailField(max_length=128, blank=True)
    contents = models.TextField(max_length=256, blank=True)
    pub_date = models.DateTimeField(default = timezone.now)
