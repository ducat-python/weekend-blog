from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect

from .models import Blog
from .forms import BlogForm

#CRUD
# Create your views here.


def blog_list(request):
    queryset = Blog.objects.all()
    context = {
        'object_list': queryset,
    }

    return render(request, 'blogs/list.html', context)



def blog_create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return HttpResponseRedirect(reverse('blogs:list'))
    else:
        form = BlogForm()
    context = {
        'form': form,
    }

    return render(request, 'blogs/create.html', context)