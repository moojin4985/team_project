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

    phone_regex = RegexValidator(regex=r'''(
    (\d{2}|\(\d{2}\)|\d{3}|\(\d{3}\))?      # 지역번호 : 2자리 또는 3자리, () 포함, 0번또는 1번  
    (|-|\.)?                                # 구분자 : 하이푼 또는 . 0번 또는 1번  
    (\d{3}|\d{4})                           # 3자리 또는 4자리 숫자  
    (\s|-|\.)                               # 구분자  
    (\d{4})                                 # 4자리 숫자  
    )''', message="")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) 

    email_regex = RegexValidator(regex=r'''(  
    ([a-zA-Z0-9._%+-]+)      # 사용자명
    @                        # @
    ([a-zA-Z0-9.-]+)         # 도메인 이름
    (\.[a-zA-Z]{2,4})        # 최상위 도메인
    )''', message="") 
    email = models.CharField(validators=[email_regex], max_length=200, blank=True) 

    contents = models.TextField()

    def __str__(self):
        return self.name