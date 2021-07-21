from django.urls import path

from . import views

urlpatterns = [
    path("", views.starting_page, name="starting-page"),
    path("posts", views.posts, name="posts-page"),
    # /posts/my-first-post "This is an example of slug and ti should contain -"
    path("posts/<slug:slug>", views.post_detail, name="post-detail-page")

]
