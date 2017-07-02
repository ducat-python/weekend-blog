from django.conf.urls import url
from .views import blog_list

urlpatterns = [

    url(r'^list/', blog_list, name='list'),
]
