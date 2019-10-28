from django.urls import path,re_path,include
from . import views 

import django.contrib.auth.urls

urlpatterns =[
    path("create",views.post_create,name="post_create"),
    #path("<int:id>/",views.post_details),
    path("<slug>/",views.post_details,name="detail_post"),
    #path(r'^details/(?P<int:id>\d+)/$', views.post_details),
    #path(r'^(?P<album_id>[0-9])/$', views.post_details, name='details'),
    path("",views.post_list,name="post_list"),
    path("<slug>/update/",views.post_update,name="update"),
    path("<slug>/delete",views.post_delete,name="delete"),
    path("create_user",views.create_user,name="create_user"),
    path("post/",include("django.contrib.auth.urls")),
]