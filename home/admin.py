from django.contrib import admin
from home.models import News, Post
# Register your models here.


#class SupportAdmin(admin.ModelAdmin):
#    list_display = ('name', 'phone_number', 'email', 'pub_date')

admin.site.register(Post)
admin.site.register(News)
#admin.site.register(Support, SupportAdmin)