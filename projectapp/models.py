from django.db import models

# Create your models here.
class Project(models.Model):
    title=models.CharField(max_length=20,null=True)
    description=models.CharField(max_length=200,null=True)
    image=models.ImageField(upload_to='project/', null=False)
    created_at=models.DateTimeField(auto_created=True, null=True)

    def __str__(self):
        return f'{self.title}'  #project 목록 출력=> 제목으로 보이게