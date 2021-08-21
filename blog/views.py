from django.shortcuts import get_object_or_404, render
from .models import Post, Author, Tag
   
# Create your views here.
def starting_page(request):
    latest_posts = Post.objects.all().order_by('-posted_date')[:3]  
    
    return render(request, "blog/index.html", {"posts":latest_posts})

def posts(request):
   
    all_posted_posts = Post.objects.all().order_by('-posted_date')
    return render(request, "blog/all-posts.html",{"all_posts": all_posted_posts})


def post_detail(reqeust, slug): 
    selected_posts = get_object_or_404(Post, slug = slug)
    
    return render(reqeust, "blog/post-detail.html", {"post": selected_posts,
    "post_tags": selected_posts.tags.all()})
