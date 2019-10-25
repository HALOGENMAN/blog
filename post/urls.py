from django.urls import path,re_path

from . import views 
urlpatterns =[
    path("create",views.post_create,name="post_create"),
    #path("<int:id>/",views.post_details),
    path("<int:id>/",views.post_details,name="detail_post"),
    #path(r'^details/(?P<int:id>\d+)/$', views.post_details),
    #path(r'^(?P<album_id>[0-9])/$', views.post_details, name='details'),
    path("",views.post_list,name="post_list"),
    path("<int:id>/update/",views.post_update,name="update"),
    path("<int:id>/delete",views.post_delete,name="delete"),
    
]