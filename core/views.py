from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm
# from requests import request
# Create your views here.

def index(request):
    return render(request,'core/index.html')


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
