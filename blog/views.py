from django.shortcuts import render
from django.http import HttpResponse
from . models import Post

posts=[
      {
      'author':'shafaq',
      'title':'Blog Post 1',
      'content':'first blog content',
      'date_posted': 'August'

       } ,
       {

       'author':'safiya',
       'title':'Blog Post 2',
       'content':'second blog content',
       'date_posted':'december'

       }


]

def home(request):
	context={'posts':Post.objects.all()}
	return render(request,'blog/home.html',context)

def about (request):
	return render(request,'blog/about.html',{'title':'about'})
