from django.shortcuts import render
from .models import Post
from django.http import Http404
from django.shortcuts import get_object_or_404

def list_view(request):
    posts = Post.objects.filter(status = Post.StatusChoices.PUBLISHED,)
    p1 = Post.objects.filter(category_id=1)
    p2 = Post.objects.filter(category_id=2)
    p3 = Post.objects.filter(category_id=3)
    p4 = Post.objects.filter(category_id=4)
    p5= Post.objects.filter(category_id=5)
    p6= Post.objects.filter(category_id=6)
    return render(request, 'list.html', {'posts':posts,'p1':p1,'p2':p2,'p3':p3,'p4':p4,'p5':p5,'p6':p6})
def detail_view(request,year, month, day, slug):
    post = get_object_or_404(Post, status=Post.StatusChoices.PUBLISHED, 
                                    publish_time__year=year, 
                                    publish_time__month=month, 
                                    publish_time__day=day, slug=slug)
    return render(request, 'detail.html', {'post': post})


def political(request):
    p1 = Post.objects.filter(category_id=1)
    return render(request,'political.html',{'p1':p1})
def economy(request):
    p2 = Post.objects.filter(category_id=2)
    return render(request,'economy.html',{'p2':p2})
def cultur(request):
    p3 = Post.objects.filter(category_id=3)
    return render(request,'cultur.html',{'p3':p3})

def sport(request):
    p4 = Post.objects.filter(category_id=4)
    return render(request,'sport.html',{'p4':p4})
def social(request):
    p5 = Post.objects.filter(category_id=5)
    return render(request,'social.html',{'p5':p5})
def art(request):
    p6 = Post.objects.filter(category_id=6)
    return render(request,'art.html',{'p6':p6})