from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Blogpost(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    yt_title = models.CharField(max_length=300)
    yt_link = models.URLField()
    content_gen = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.yt_title