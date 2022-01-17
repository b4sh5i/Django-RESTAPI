from django.db import models

# Create your models here.
class Post(models.Model):
    idx = models.IntegerField(verbose_name='인덱스')
    head = models.CharField(max_length=255, verbose_name='제목')
    content = models.TextField(verbose_name='내용')
