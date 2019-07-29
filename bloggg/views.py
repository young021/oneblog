from django.shortcuts import render,redirect,get_object_or_404
from .models import Blog
from django.utils import timezone

# Create your views here.


def home(request):
   blogs=Blog.objects
   return render(request,'log.html',{'blogs':blogs})  

def detail(request,blog_id):
    detail = get_object_or_404(Blog, pk=blog_id)   
    return render(request,'detail.html',{'detail':detail})

def new(request):
    return render(request,'new.html')    


def create(request):
    blog=Blog()
    blog.title=request.GET['title']
    blog.body=request.GET['body']
    blog.pub_date=timezone.datetime.now()
    blog.save()
    return redirect('/blog/' +str(blog.id))

def delete(request,blog_id):
   blog_delete = get_object_or_404(Blog, id= blog_id)
   blog_delete.delete()
   return redirect('log') 


