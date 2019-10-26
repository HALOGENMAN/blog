from django.db import models
from django.urls import  reverse
import os

def upload_location(instance,filename):#this is also new ,,read it
    return os.path.join("photos",str(instance.pk),filename)

class Post(models.Model):
    title = models.CharField(max_length=120)
    #image = models.FileField(null=True,blank=True)
    image = models.ImageField(upload_to=upload_location,null=True,blank=True,width_field="width_f",height_field="height_f") # this thing is need to be readed both are going same thing
    width_f = models.IntegerField(default=0)# not necrssary to give user input
    height_f = models.IntegerField(default=0)# not necesary to give user input
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