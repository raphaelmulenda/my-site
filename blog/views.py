import blog
from django.shortcuts import get_object_or_404, render
from .models import Post, Author, Tag
from django.views.generic import ListView, DetailView
from .form import CommentForm
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse

   
# Create your views here.

class StatingPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-posted_date"] # this will oder the bellow data 
    context_object_name = "posts" #This will rename or presnt teh output data in posts 
    
    def get_queryset(self): #This function will fesh all data
        queryset = super().get_queryset()
        data = queryset[:3] # This code will limited the number of posts to 3
        return data
    
    
# def starting_page(request):
#     latest_posts = Post.objects.all().order_by('-posted_date')[:3]  
    
#     return render(request, "blog/index.html", {"posts":latest_posts})


class AllPostsView(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    ordering = ["-posted_date"] 
    context_object_name = "all_posts"
        
    
    
# def posts(request):
   
#     all_posted_posts = Post.objects.all().order_by('-posted_date')
#     return render(request, "blog/all-posts.html",{"all_posts": all_posted_posts})

# class SinglePostView(DetailView): #detailview is allow us to create view that show details , detail views can search data by slug or ID if we sepcify it as dynamic segment in urls so not need to specify this and if tenresult doent mucht it will serve the 404page
#     template_name = "blog/post-detail.html"
#     model = Post
    
#     def get_context_data(self, **kwargs) :
#         context = super().get_context_data(**kwargs)
#         context ["post_tags"] = self.object.tags.all() #This will take the selected object and wll tale all his tags in the object 
#         context["comment_form"] = CommentForm() # This will create a CommentForm 
#         return context
    
class SinglePostView(View): #detailview is allow us to create view that show details , detail views can search data by slug or ID if we sepcify it as dynamic segment in urls so not need to specify this and if tenresult doent mucht it will serve the 404page
   
    def is_stored_posts(self,request,post_id):
        stored_posts= request.session.get("stored_posts")
        if stored_posts is not None:
            is_saved_for_later = post_id in stored_posts
        else:
            is_saved_for_later = False
        
        return is_saved_for_later
        
    def get(self,request,slug):
        post = Post.objects.get(slug = slug)
        
        context = {
            "post":post,
            "post_tags":post.tags.all(),
            "comment_form":CommentForm(),
            "comments": post.comments.all().order_by("-id"), #this will oder by Id in descen order due to the sign (-)
            "saved_for_later": self.is_stored_posts(request,post.id)
        }
        return render(request, "blog/post-detail.html", context)

    def post(self,request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug = slug)
        if comment_form.is_valid():
            comment =comment_form.save(commit=False) #This will take user inpute without   saving he data
            comment.post = post # This will add post the one we excluded in the CommentForm and it will be added to the above code
            comment.save() #This will not save manully the complute data to the DB
            return HttpResponseRedirect(reverse("post-detail-page",args=[slug]))
        
        context = {
            "post":post,
            "post_tags":post.tags.all(),
            "comment_form":CommentForm(),
            "comments": post.comments.all().order_by("-id"),
            "saved_for_later": self.is_stored_posts(request,post.id) 
        }
        return render(request, "blog/post-detail.html", context)
    
    
# def post_detail(reqeust, slug): 
#     selected_posts = get_object_or_404(Post, slug = slug)
    
#     return render(reqeust, "blog/post-detail.html", {"post": selected_posts,
#     "post_tags": selected_posts.tags.all()})

class ReadLaterView(View):
    def get(self, request):
        stored_posts = request.session.get("stored_posts")
       
        context = {}
        
        if stored_posts is None or len(stored_posts) == 0:
            context["posts"] = []
            context["has_posts"] = False
        else:
            posts = Post.objects.filter(id__in=stored_posts)
            context["posts"]= posts
            context["has_posts"] = True
        return render(request, "blog/stored-posts.html", context)
        
    def post(self,request):
        stored_posts = request.session.get("stored_posts")
        
        if stored_posts is None:
            stored_posts = []
            
        post_id = int(request.POST["post_id"])
        
        if post_id not in stored_posts:
            stored_posts.append(post_id)
            
        else: 
            stored_posts.remove(post_id)
            
        request.session["stored_posts"] = stored_posts # this code will now save the post to the stored one
        
        return HttpResponseRedirect("/")