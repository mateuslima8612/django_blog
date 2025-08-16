from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/id/<int:pk>/', views.post_detail, name='post-detail')
]