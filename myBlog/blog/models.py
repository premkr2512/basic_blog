from django.core.exceptions import MultipleObjectsReturned
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.utils.timezone import now
# Create your models here.
class Contact(models.Model):
    S_no=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=20)
    phone_no=models.CharField(max_length=11)
    email=models.CharField(max_length=100)
    problem=models.TextField()
    date=models.DateField(default=datetime.now, blank=True)
    def __str__(self):
        return "Message from" +self.Name

class Post(models.Model):
    S_no=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    content=models.TextField()
    author=models.CharField(max_length=10)
    slug=models.CharField(max_length=100)
    timestamp=models.DateTimeField(blank=True)
    def __str__(self):
        return self.title + "by" + self.author

class BlogComment(models.Model):
    sno=models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE,null=False)
    timestamp=models.DateTimeField(default=now)