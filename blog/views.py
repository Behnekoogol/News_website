from django.shortcuts import redirect, render
from .models import Post, Category
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView


def list_view(request):
    posts = Post.objects.filter(status = Post.StatusChoices.PUBLISHED,) 
    return render(request, 'list.html', {'posts':posts})



def detail_view(request,year, month, day, slug):
    post = get_object_or_404(Post, status=Post.StatusChoices.PUBLISHED, 
                                    publish_time__year=year, 
                                    publish_time__month=month, 
                                    publish_time__day=day, slug=slug)
    return render(request, 'detail.html', {'post': post})
    


# def category(request, category):
#     # Retrieve the articles for this category from your database
#     posts = Post.objects.filter(status = Post.StatusChoices.PUBLISHED,)
#     category = Category.objects.all()
#     context = {
#         'category': Category,
#         'post': posts,
#     }
#     return render(request, 'category.html', context)



# def politics(request):
#     # Instead of rendering politics.html, redirect to the category view
#     return redirect('category', category='politics')


# def economy(request):
#     # Instead of rendering politics.html, redirect to the category view
#     return redirect('category', category ='economic')



# def sport(request):
#     # Instead of rendering politics.html, redirect to the category view
#     return redirect('category', category ='sport')



# def social(request):
#     # Instead of rendering politics.html, redirect to the category view
#     return redirect('category', category ='social')




# def political(request):
#     p1 = Post.objects.filter(category_id=1)
#     return render(request,'political.html',{'p1':p1})
# def economy(request):
#     p2 = Post.objects.filter(category_id=2)
#     return render(request,'economy.html',{'p2':p2})
# def cultur(request):
#     p3 = Post.objects.filter(category_id=3)
#     return render(request,'cultur.html',{'p3':p3})

# def sport(request):
#     p4 = Post.objects.filter(category_id=4)
#     return render(request,'sport.html',{'p4':p4})
# def social(request):
#     p5 = Post.objects.filter(category_id=5)
#     return render(request,'social.html',{'p5':p5})
# def art(request):
#     p6 = Post.objects.filter(category_id=6)
#     return render(request,'art.html',{'p6':p6})




class CategoryListView(TemplateView):
    template_name = 'category_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_slug = kwargs['category_slug']
        category = get_object_or_404(Category, title=category_slug)
        posts = Post.objects.filter(category=category)
        context['category'] = category
        context['posts'] = posts
        return context
