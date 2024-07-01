from django.shortcuts import render,redirect
from .forms import PostCreationForm
from .models import Post
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.core.paginator import Paginator

# Create your views here.
# def index(request):
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
    # posts=Post.objects.all()

    # context={
    #     'posts':posts,
    #     'title':'Home Page '
    # }

    # return render(request,'posts/home.html',context)

class HomePageView(View):

    template_name="posts/home.html"

    def get(self,request):
        posts=Post.objects.all()

        paginator=Paginator(posts,3)

        page_number=request.GET.get('page')

        page_obj=paginator.get_page(page_number)

        context={
            'posts':page_obj
        }
        return render(request,self.template_name,context)

# def about(request):
#     context={
#         "title":"About Page "
#     }
#     return render(request,'posts/about.html',context)

class AboutPageView(HomePageView):
    template_name="posts/about.html"

def services(request):
    context={
        "title":"Services Page "
    }
    return render(request,'posts/services.html',context)




# @login_required
# def create_post(request):

#     form=PostCreationForm()

#     if request.method =="POST":
#         form=PostCreationForm(request.POST, request.FILES)

#         if form.is_valid():
#             form.save()

#         return redirect('posts/posts_home')
    
#     context={'form':form,'title':'Create_post'}
#     return render(request,'posts/createpost.html',context)

@method_decorator(login_required,'dispatch')
class CreatePostView(View):
    template_name='posts/createpost.html'
    form_class=PostCreationForm
    initial_values={"key":"value"}

    def get(self,request):
        form=self.form_class(initial=self.initial_values)

        context={
            "form":form
        }

        return render(request,'posts/createpost.html',context)


    def post(self,request):
        form=self.form_class(request.POST,request.FILES)

        if form.is_valid():
            form.save()

            return redirect('posts_home')


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

            return redirect('posts_home')

    context={
        'form':form
    }
    return render(request,'posts/update.html',context)
    
    

