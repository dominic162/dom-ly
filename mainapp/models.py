from django.db import models
from django.contrib.auth.models import User

class urlshort(models.Model):
    original_url=models.URLField(blank=False)
    short_url=models.CharField(blank=False,max_length=8)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.original_url