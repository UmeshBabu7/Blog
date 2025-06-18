from django.urls import path
from .import views
from django.contrib.auth.decorators import login_required

app_name='posts'

urlpatterns = [
    path('',views.HomePageView.as_view(),name="posts_home"),
    path('about/',views.about,name="posts_about"),
    path('services/',views.services,name="posts_services"),
    # path('create_post/',views.create_post,name="create_post"),
    path('create_post',views.CreatePostView.as_view(),name='create_post'),
    path('post/<int:post_id>',views.post_detail,name='post_detail'),
    path('post/update/<int:post_id>/',views.update_post,name='update_post'),
    path('search/', views.SearchView.as_view(), name='search')
]
