from django.conf.urls import url
from .views import blog_list, blog_create, blog_update

urlpatterns = [

    url(r'^list/', blog_list, name='list'),
    url(r'^create/', blog_create, name='create'),
    url(r'^(?P<pk>\d+)/update/', blog_update, name='update'),
]
