from django.db import models
from django.urls import  reverse
import os
from django.contrib.auth.models import User
from django.db.models.signals import pre_save # need to be learned /// cheeckout the documentation
from django.utils.text import slugify

def upload_location(instance,filename):# this is also new ,,read it
    return os.path.join("photos",instance.slug,filename)# it will save when itis updated

class Post(models.Model):
    user = models.ForeignKey(User,default=1,on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    #image = models.FileField(null=True,blank=True)  //// "%upload_location" is used to save files according to date
    image = models.ImageField(upload_to="%Y/%m/%d",null=True,blank=True,width_field="width_f",height_field="height_f") # this thing is need to be readed both are going same thing
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
        return reverse("detail_post",kwargs={"slug" : self.slug})
        # return "/post/"(self.id)
    
    class Meta:
        ordering = ["-timestap","-update"] # in this it is showing about ordered by but by using meta classs


def create_slug(instance,new_slug=None):
    slug=slugify(instance.title)
    if new_slug is not None:
        slug=new_slug
    qs = Post.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug,qs.first().id)
        return create_slug(instance,new_slug=new_slug)#recursion in python
    return slug

# def pre_save_post_reciver(sender,instance,*args,**kwargs):
    #    slug = slugify(instance.title) # suppose title is "Tesla 1" --> "tesla-1"//slug
    #    exists = Post.objects.filter(slug=slug).exists()
    #    if exists:
    #        slug = os.path.join(slug,str(instance.id))

    #    instance.slug=slug

def pre_save_post_reciver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_reciver,sender=Post)