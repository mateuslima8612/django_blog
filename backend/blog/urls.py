from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/id/<int:pk>/', views.post_detail, name='post-detail'),
    path('posts/', views.posts, name='posts'),
    path('posts/<int:page>', views.posts, name='posts-paginated'),
    path('about', views.about, name='about')
]