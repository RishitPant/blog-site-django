from django.urls import path
from . import views
from .views import DeletePostView, AddPostView, UpdatePostView


urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:pk>', views.post, name='post'),
    path('about', views.about, name='about'),
    path('post/about_us', views.about_us, name='about_us'),
    path('contact_us', views.contact_us, name='contact_us'),
    path('post/contactus', views.contactus, name='contactus'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('create_post', AddPostView.as_view(), name='create_post'),
    path('post_delete', views.post_delete, name='post_delete'),
    path('post/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('post/<int:pk>/remove', DeletePostView.as_view(), name='delete_post'),
]