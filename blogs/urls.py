from django.conf.urls import url
from .views import blog_list, blog_create

urlpatterns = [

    url(r'^list/', blog_list, name='list'),
    url(r'^create/', blog_create, name='create'),
]
