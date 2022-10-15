from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse


posts = [
    {
        'author' : 'Adil. Ghafari',
        'title': 'Blog Post1',
        'content' : 'First post',
        'date_posted': 'Oktober 08,2022'

    },
    {

    'author' : 'Amanah. Ghafari',
    'title': 'Blog Post2',
    'content' : 'Second post',
    'date_posted': 'Oktober 10,2022'
    
    }  
       
]

def home(request):
    
    context = {
        'posts': posts
        }
    return render(request,'blog/home.html',context)



def about(request):
    
    return render(request,'blog/about.html',{'title':'about'})


 