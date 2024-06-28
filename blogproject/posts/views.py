from django.shortcuts import render

# Create your views here.
def index(request):
    posts=[
        {
            "id":1,
            "title":"Python",
            "author":"Umesh Tamang"
        },
         {
            "id":2,
            "title":"Django",
            "author":"Ramesh Tamang"
        },
         {
            "id":3,
            "title":"Mysql",
            "author":"Babu Tamang"
        }
    ]

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
