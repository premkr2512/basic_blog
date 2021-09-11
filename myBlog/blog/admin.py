from django.contrib import admin

# Register your models here.
from . models import Contact, Post,BlogComment
admin.site.register(Contact)
admin.site.register(Post)
admin.site.register(BlogComment)