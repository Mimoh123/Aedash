from telnetlib import STATUS
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect, render,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm,CommentForm
from .models import Post,Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core import serializers
from django.http import HttpResponse
from django.http import JsonResponse



# from requests import request
# Create your views here.

def index(request):


    
    object_list = Post.objects.filter(status = 'published')
    paginator = Paginator(object_list,3) # 3 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        #if the page is not an integer, deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        #if the page is out of range, deliver the last page of results
        posts = paginator.page(paginator.num_pages)
    
    
    return render(request,'core/index.html',{'posts':posts,'page':page,})


#implementing authentication
@login_required
def locked_page(request):
    return render(request,'core/locked.html')

def register(request):
    if request.method == "POST":
        user_form  = UserRegistrationForm(data = request.POST)
        if user_form.is_valid():
            #create a new user object but avoid saving it yet
            new_user = user_form.save(commit = False)
            #set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            #save the User object
            new_user.save()
            return redirect('login')
    else:
        user_form = UserRegistrationForm()
    return render(request,'registration/user_register.html',{'user_form':user_form})



def post_detail(request,year,month,day,post):
    post = get_object_or_404(Post,slug= post,status='published',publish__year = year,publish__day = day)
    feature = Post.objects.filter(featured = True)
    #comments which are active
    comments = post.comments.filter(active = True)

    new_comment= None
    # path_to_
    if request.method == "POST":
        # A comment was posted
        username = request.POST['uname']
        email = request.POST['email']
        body = request.POST['body']
        comment = Comment.objects.create(post = post,name = username,email= email,body = body)
        comment.save()
        return HttpResponseRedirect(post.get_absolute_url())
            #Create comment object but don't save to the database yet
            # new_comment = comment_form.save(commit=False)
            
            #assign the current post to the database
            # new_comment.post = post
            
            #Save the comment to the database
            # new_comment.save()
    
    return render(request,
        'core/post_detail.html',
        {'post': post,'comments':comments,'new_comment':new_comment,'featured':feature})
        
def search(request):
    data = list(Post.objects.values())
    return render(request,'base.html',{'data':data})
