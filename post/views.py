from django.shortcuts import render,get_object_or_404,redirect,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import Post
from .forms import PostForms,create_userForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm#,LoginUserForm
from django.core.paginator import Paginator
from django.contrib.auth.models import User,auth

# Create your views here.
def post_update(request,slug=None):
    instance = get_object_or_404(Post,slug=slug)
    form = PostForms(request.POST or None,request.FILES or None,instance=instance)#it is use for updating 
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

def post_details(request,slug=None):
    instance = get_object_or_404(Post,slug=slug)
    context = {
        "obj":instance,
    }
    return render(request,"post_details.html",context)

def post_create(request):
    #if not request.user.is_authenticated():
    #    raise Http404
    form = PostForms(request.POST or None,request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        #print(form.cleaned_data.get("title"))
        instance.user=request.user
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

def post_delete(request,slug=None):
    instance = get_object_or_404(Post,slug=slug)
    instance.delete()
    messages.success(request,"Successifully DLEATED")
    return redirect("post_list")#in this it is redirecting by the use of name from url page




#def listing(request):  /// pagination content in detail
#    contact_list = Post.objects.all()
#    paginator = Paginator(contact_list, 25) # Show 25 contacts per page
#    page = request.GET.get('page')
#    contacts = paginator.get_page(page)
#    return render(request, 'index.html', {'object_list': contacts})

def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,"login success")
            return redirect("{% url 'post_list' %}")
        else:
            messages.success(request,"not able to login")
            return render(request,"login.html",{})
        
    return render(request,"login.html",{})

def create_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            
        return redirect("post_list")
        
        
    else:
        form = UserCreationForm()
        context = {
            "form" : form,
        }
        return render(request,"create_form_user.html",context)

