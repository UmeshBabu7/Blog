from django.shortcuts import render,redirect
from .forms import PostCreationForm
from .models import Post
from django.contrib.auth.decorators import login_required

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

    return render(request,'posts/home.html',context)

def about(request):
    context={
        "title":"About Page "
    }
    return render(request,'posts/about.html',context)

def services(request):
    context={
        "title":"Services Page "
    }
    return render(request,'posts/services.html',context)

@login_required
def create_post(request):

    form=PostCreationForm()

    if request.method =="POST":
        form=PostCreationForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

        return redirect('posts/posts_home')
    
    context={'form':form,'title':'Create_post'}
    return render(request,'posts/createpost.html',context)

def post_detail(request,post_id):
    post=Post.objects.get(pk=post_id)

    context={'post':post}
    return render(request,'posts/post_detail.html',context)

@login_required
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

            return redirect('posts/posts_home')

    context={
        'form':form
    }
    return render(request,'posts/update.html',context)
    
    

