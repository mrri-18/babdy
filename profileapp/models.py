from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile') #1:1 매칭, 객체가 탈퇴하면 프로필도 같이 삭제됨.

    image=models.ImageField(upload_to='profile/', null=True) #media/profile 경로 아래에 이미지가 저장됨.
    nickname=models.CharField(max_length=20, unique=True, null=True) # nickname은 유일해야함.
    message=models.CharField(max_length=100, null=True)