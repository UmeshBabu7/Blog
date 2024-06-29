from django.shortcuts import render,redirect
from .forms import PostCreationForm
from .models import Post

# Create your views here.
def index(request):
    # posts=[
    #     {
    #         "id":1,
    #         "title":"Python",
    #         "author":"Umesh Tamang"
    #     },
    #      {
    #         "id":2,
    #         "title":"Django",
    #         "author":"Ramesh Tamang"
    #     },
    #      {
    #         "id":3,
    #         "title":"Mysql",
    #         "author":"Babu Tamang"
    #     }
    # ]
    posts=Post.objects.all()

    context={
        'posts':posts,
        'title':'Home Page '
    }

    return render(request,'home.html',context)

def about(request):
    context={
        "title":"About Page "
    }
    return render(request,'about.html',context)

def services(request):
    context={
        "title":"Services Page "
    }
    return render(request,'services.html',context)

def create_post(request):
    form=PostCreationForm()

    if request.method =="POST":
        data=request.POST

        title=data["title"]
        content=data["content"]
        author=data["author"]

        new_post=Post(
            title=title,content=content,author=author)
        new_post.save()

        return redirect('posts_home')
    context={'form':form}
    return render(request,'createpost.html',context)

