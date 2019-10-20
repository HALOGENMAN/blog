from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Post

# Create your views here.
def post_update(request):
    return HttpResponse("<h1>shayak</h1>")

def post_details(request,id=None):
    instance = get_object_or_404(Post,id=id)
    context = {
        "obj":instance,
    }
    return render(request,"post_details.html",context)

def post_create(request):
    return HttpResponse("<h1>shayak</h1>")

def post_list(request):
    queryset = Post.objects.all()
    context = {
        "object_list":queryset
    }
    return render(request,"index.html",context)

def post_delete(request):
    return HttpResponse("<h1>shayak</h1>")