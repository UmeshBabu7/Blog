from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts=[
    {
        "id":1,
        "title":"Python",
        "author":"Umesh"
    },
    {
        "id":2,
        "title":"Javascript",
        "author":"Ramesh"
    },
    {
        "id":3,
        "title":"Dotnet",
        "author":"Ishan"
    },
]

def index(request):
    context={
        'posts':posts,
        'title':"Home Page"
    }
    return render(request,'index.html',context)


def return_all_posts(request):
    return HttpResponse(str(posts))

def return_one_post(request,post_id):
    for post in posts:
        if post["id"] ==post_id:
            return HttpResponse(str(post))
        
    return HttpResponse("Not found")


def about(request):
    context={
        'title':"About page"
    }
    return render(request,'about.html',context)


def services(request):
    context={
        'title':'services page'
    }
    return render(request,'services.html',context)
