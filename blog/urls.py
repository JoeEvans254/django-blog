from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import logout_view

urlpatterns = [
     path('', views.blog_list, name='home'),

    # Auth
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('create/', views.create_blog, name='create_blog'),
    path('blog/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('logout/', logout_view, name='logout'),
    

    
]
