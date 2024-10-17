from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import PostCreationForm
from .models import Post

# Create your views here.



def index(request):
    posts=Post.objects.all()
    context={
        'posts':posts
    }
    return render(request,'index.html',context)


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


def create_post(request):
    form=PostCreationForm()

    if request.method =="POST":
        form = PostCreationForm(request.POST , request.FILES)

        if form.is_valid():
            form.save()
            return redirect('posts_home')
   
    context={
        'form':form

    }
    return render(request,'createpost.html',context)


def post_detail(request,post_id):
    post=Post.objects.get(pk=post_id)
    context={'post':
             post}
    return render(request,'post_detail.html',context)


def update_post(request,post_id):
    post_to_update=Post.objects.get(pk=post_id)
    form=PostCreationForm(instance=post_to_update)

    if request.method == "POST":
        form=PostCreationForm(instance=post_to_update,
            data=request.POST,
            files=request.FILES
        )

        if form.is_valid():
            form.save()

            return redirect('posts_home')

    context={
        'form':form
    }

    return render(request,'update.html',context)
