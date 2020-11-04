from django.core.checks import messages
from django.core.checks.messages import ERROR
# from Car_Review.settings import MAILCHIMP_API_KEY, MAILCHIMP_DATA_CENTER, 
from django.shortcuts import render, redirect,get_object_or_404
from .models import Blog,Newsletter,ProfileCard
from .forms import CommentForm,NewsletterForm,ContactForm
import time
from django.conf import settings
import json 
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from .utils import SendSubscribeMail
from django.http import HttpResponse, JsonResponse,HttpResponseRedirect

# MAILCHIMP_API_KEY = settings.MAILCHIMP_API_KEY
# MAILCHIMP_DATA_CENTER = settings.MAILCHIMP_DATA_CENTER
# MAILCHIMP_EMAIL_LIST = settings.MAILCHIMP_EMAIL_LIST

# api_url = f'https://{MAILCHIMP_DATA_CENTER}.api.mailchimp.com/3.0'
# members_endpoint =f'{api_url}/lists/{MAILCHIMP_EMAIL_LIST}/mambers'

# Create your views here.
# def subscribe(request):
#     if request.method == 'POST':
#         email = request.POST['email_id']
#         email_qs = Newsletter.objects.filter(email_id = email)
#         if email_qs.exists():
#             data = {"status" : "404"}
#             return JsonResponse(data)
#         else:
#             Newsletter.objects.create(email_id = email)
#             SendSubscribeMail(email) # Send the Mail, Class available in utils.py

#     return HttpResponse("/")
# def subscribe(email):
#     data ={
#         'email_address':email,
#         "status":"subscribed"
#     }
#     r= request.post(
#         members_endpoint,
#         auth = ("",MAILCHIMP_API_KEY),
#         data =json.dumps(data)
#     )
#     return r.status_code, r.json()

def IndexPage(request):
    blogs = Blog.objects.all()
    sorted_blog = Blog.objects.order_by('-date')[:3]


    return render(request, 'blogApp/index.html',{'blogs':blogs,'sorted_blog':sorted_blog})


def BlogPage(request):
    blogs = Blog.objects.order_by('-date')
    latest_blogs = Blog.objects.order_by('-date')[:10]
    return render(request, 'blogApp/blog.html',{'blogs':blogs,'latest_blogs':latest_blogs})


def PostPage(request,blog_id):
    #Save views
    # blog_object = Blog.objects.filter(id=id)
    # blog_object.post_views = blog_object.post_views + 1
    # blog_object.save()
    # time.sleep(5000)
    #----------
    blogs = Blog.objects.order_by('-date')
    latest_blogs = Blog.objects.order_by('-date')[:10]
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

    return render(request, 'blogApp/post.html',{'blog':blog,'blogs':blogs,'comment_form':comment_form,'latest_blogs':latest_blogs})

def AboutPage(request):
    cards = ProfileCard.objects.all()
    return render(request,'blogApp/about.html',{'cards':cards})


def contactPage(request):
    contact_form = ContactForm()
    if request.method ==  'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            print("VALLLIIIIID")
            
            subject =f'Message From {contact_form.cleaned_data["name"]}'
            message = contact_form.cleaned_data["message"]
            sender = contact_form.cleaned_data["email"]
            recipient = ['testerpython7@gmail.com']
            contact_form.save()
           
            try:
                send_mail(subject,message,sender,recipient,fail_silently=False)
            except BadHeaderError:
                return HttpResponse("Invalid header Email")
            return HttpResponse("Email sent succesfully")
    return render (request,'blogApp/contact.html',{'contact_form':contact_form})

#    if request.method == "POST":
#         addcomment = CommentForm(request.POST)
#         if addcomment.is_valid():
#             print("valid")
#             addcomment.save()
#     addcomment = CommentForm()