from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    return render(request,'core/index.html')


#implementing authentication
@login_required
def locked_page(request):
    return render(request,'core/locked.html')