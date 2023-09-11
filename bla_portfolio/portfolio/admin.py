from django.contrib import admin
from .models import *

# Register your models here.

class BlogsAdmin(admin.ModelAdmin):
    list_display=['title', 'authname','timeStamp']
    list_filter=['authname']
    search_fields=['title','authname']

admin.site.register(Blogs, BlogsAdmin)