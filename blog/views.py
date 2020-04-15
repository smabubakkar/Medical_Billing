from django.shortcuts import render
from .models import Post
# Create your views here.
def stock(request):
    posts=Post.objects.all()
    return render(request,'blog/stock.html',{'posts':posts})

