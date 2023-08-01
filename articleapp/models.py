from django.contrib.auth.models import User
from django.db import models

from projectapp.models import Project


# Create your models here.
class Article(models.Model):
    writer=models.ForeignKey(User, on_delete=models.SET_NULL, related_name='article', null=True) #user 객체의 아티클에 접근할 때 writer 사용.
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, related_name='article', null=True)
    title=models.CharField(max_length=200, null=True)
    image=models.ImageField(upload_to='article/', null=False)
    content=models.TextField(null=True) #긴 내용
    created_at=models.DateField(auto_created=True, null=True)
