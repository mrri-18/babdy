from django.contrib.auth.models import User
from django.db import models

from projectapp.models import Project


# Create your models here.
class Subscription(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscription')
    project=models.ForeignKey(Project, on_delete=models.CASCADE, related_name='subscription')

    class Meta:
        unique_together=('user', 'project') #어떤 유저가 한 프로젝트를 딱 한번만 구독할 수 있도록 함.