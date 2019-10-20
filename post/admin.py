from django.contrib import admin
from .models import Post
# Register your models here.

class AdminModelPost(admin.ModelAdmin):
    list_display=["title","update","timestap"]
    list_display_links=["update"]
    list_filter=["update","timestap"]
    list_editable=["title"]
    search_fields=["title","content"]
    class Meta:
        model = Post

admin.site.register(Post,AdminModelPost)