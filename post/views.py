from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Post
from .forms import PostForms

# Create your views here.
def post_update(request):
   pass

def post_details(request,id=None):
    instance = get_object_or_404(Post,id=id)
    context = {
        "obj":instance,
    }
    return render(request,"post_details.html",context)

def post_create(request):
    form = PostForms(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        print(form.cleaned_data.get("title"))
        instance.save()
    
    #if request.method=="POST":
    #   title=request.POST.get("title")
    #    content=request.POST.get("content")
    #   Post.objects.create(title=title,content=content)
    
    context={
        "form":form,
    }
    return render(request,"post_forms.html",context)

def post_list(request):
    queryset = Post.objects.all()
    context = {
        "object_list":queryset
    }
    return render(request,"index.html",context)

def post_delete(request):
    return HttpResponse("<h1>shayak</h1>")

