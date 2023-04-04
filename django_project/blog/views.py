#from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.

class PostList(ListView):
    model = Post
    #template_name = 'blog/index.html'
    ordering = '-pk'

class PostDetail(DetailView):
    mode = Post

'''
def index(request):
    posts = Post.objects.all().order_by('pk')

    return render(
        request,
        'blog\index.html',
        {
            'posts' : posts,
        }
    )

'''

def single_post_page(request, post_num):
    post = Post.objects.get(pk=post_num)

    return render(
        request,
        'blog/single_post_page.html',
        {
            'post' : post,
        }
    )


