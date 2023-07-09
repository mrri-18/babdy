from django.db import models

# Create your models here.
class Helloworld(models.Model):
    text=models.CharField(max_length=255, null=False) #문자열, 반드시 null 안됨
