from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import PostCreationForm
from .models import Post
from django.contrib.auth.decorators import login_required
from django.views import View
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator
from django.db import models

# Create your views here.



# def index(request):
#     posts=Post.objects.all()
#     context={
#         'posts':posts
#     }
#     return render(request,'index.html',context)

class HomePageView(View):
    template_name="index.html"

    def get(self,request):
        posts=Post.objects.all()

        paginator=Paginator(posts,3)
        page_number=request.GET.get('page')
        print(page_number)
        page_obj=paginator.get_page(page_number)

        context={
        'posts':page_obj
    }
        return render(request,self.template_name,context)


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


@method_decorator(login_required,'dispatch')
class CreatePostView(View):
    template_name='createpost.html'
    form_class=PostCreationForm
    initial_values={"key":"value"}

    def get(self,request):
        form=self.form_class(initial=self.initial_values)
        context={
            "form":form
        }
        return render(request,'createpost.html',context)
    def post(self,request):
        form=self.form_class(request.POST,request.FILES)

        if form.is_valid():
            form.save()

            return redirect('posts:posts_home')





def post_detail(request,post_id):
    post=Post.objects.get(pk=post_id)
    context={'post':
             post}
    return render(request,'post_detail.html',context)


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
            return redirect('posts:posts_home')

    context={
        'form': form,
        'post': post_to_update
    }

    return render(request,'update.html',context)

class SearchView(View):
    template_name = 'index.html'

    def get(self, request):
        query = request.GET.get('q', '')
        if query:
            posts = Post.objects.filter(
                models.Q(title__icontains=query) | 
                models.Q(content__icontains=query)
            )
        else:
            posts = Post.objects.all()

        paginator = Paginator(posts, 3)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'posts': page_obj,
            'query': query
        }
        return render(request, self.template_name, context)
