from djongo import models
from django.utils import timezone
# Create your models here.


class Post(models.Model):
    auther = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    pub_date = models.DateTimeField(default = timezone.now)
    mainphoto = models.ImageField(blank=True, null=True) #

    def __str__(self):
        return self.title