from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Node(models.Model):
    idx = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '[{}] {}'.format(self.idx, self.title)