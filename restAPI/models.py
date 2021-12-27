from django.db import models
from django.utils import timezone

class b4sh5i_data(models.Model):
    idx = models.IntegerField(default=0)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name