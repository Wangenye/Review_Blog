from django.shortcuts import render, redirect,get_object_or_404
from .models import Blog
from .forms import CommentForm

# Create your views here.


def IndexPage(request):
    blogs = Blog.objects.all()

    return render(request, 'blogApp/index.html',{'blogs':blogs})


def BlogPage(request):
    blogs = Blog.objects.all()
    return render(request, 'blogApp/blog.html',{'blogs':blogs})


def PostPage(request,blog_id):
    blogs = Blog.objects.all()
    blog = get_object_or_404(Blog, pk=blog_id)

    # comments = blog.comments.filter(active=True)
    new_comment = None

    # # Posted comments 
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = blog
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, 'blogApp/post.html',{'blog':blog,'blogs':blogs,'comment_form':comment_form})


#    if request.method == "POST":
#         addcomment = CommentForm(request.POST)
#         if addcomment.is_valid():
#             print("valid")
#             addcomment.save()
#     addcomment = CommentForm()