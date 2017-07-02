from django.shortcuts import render

from .models import Blog


# Create your views here.


def blog_list(request):
    queryset = Blog.objects.all()
    context = {
        'object_list': queryset,
    }

    return render(request, 'blogs/list.html', context)
