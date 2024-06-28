from django.urls import path
from .import views
urlpatterns = [
    path('',views.index,name='posts_home'),
    path('about/',views.about,name='posts_about'),
    path('services/',views.services,name='posts_services')
]
