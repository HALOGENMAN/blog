from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    update = models.DateTimeField(auto_now=True,auto_now_add=False)
    timestap = models.DateTimeField(auto_now=True,auto_now_add=False)

    def __unicode__(self):
        return self.title
    
    def __str__(self):
        return self.title