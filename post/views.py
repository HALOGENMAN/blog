from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import Post
from .forms import PostForms
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.
def post_update(request,id=None):
    instance = get_object_or_404(Post,id=id)
    form = PostForms(request.POST or None,instance=instance)#it is use for updating 
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request,"<a href=" "> item </a> updated",extra_tags="html_safe")
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "obj":instance,
        "form":form
    }
    return render(request,"post_forms.html",context)

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
        messages.success(request,"Successifully Created")
        return HttpResponseRedirect(instance.get_absolute_url())#important for redirecting
    
    #if request.method=="POST":
    #   title=request.POST.get("title")
    #    content=request.POST.get("content")
    #   Post.objects.create(title=title,content=content)
   
    context={
        "form":form,
    }
    return render(request,"post_forms.html",context)

def post_list(request):
    queryset = Post.objects.all() #.order_by("-timestap")  /// instad of using meta class we can use this function
    paginator = Paginator(queryset, 5)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    context = {
        "object_list":contacts
    }
    return render(request,"index.html",context)

def post_delete(request,id=None):
    instance = get_object_or_404(Post,id=id)
    instance.delete()
    messages.success(request,"Successifully DLEATED")
    return redirect("post_list")#in this it is redirecting by the use of name from url page




def listing(request):
    contact_list = Post.objects.all()
    paginator = Paginator(contact_list, 25) # Show 25 contacts per page

    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    return render(request, 'index.html', {'object_list': contacts})