from django.db import models
from django.urls import  reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    update = models.DateTimeField(auto_now=True,auto_now_add=False)
    timestap = models.DateTimeField(auto_now=False,auto_now_add=True)

    def __unicode__(self):
        return self.title
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("detail_post",kwargs={"id" : self.id})
        #return "/post/"(self.id)
    
    class Meta:
        ordering = ["-timestap","-update"] # in this it is showing about ordered by but by using meta classs