from django.shortcuts import render
from .models import Post
from django.http import Http404
from django.shortcuts import get_object_or_404

def list_view(request):
    posts = Post.objects.filter(status = Post.StatusChoices.PUBLISHED,) 
    return render(request, 'list.html', {'posts':posts})



def detail_view(request,year, month, day, slug):
    post = get_object_or_404(Post, status=Post.StatusChoices.PUBLISHED, 
                                    publish_time__year=year, 
                                    publish_time__month=month, 
                                    publish_time__day=day, slug=slug)
    return render(request, 'detail.html', {'post': post})
    
