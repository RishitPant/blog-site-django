from django import urls
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('blogApp.urls')),
    path('post/<int:pk>', include('blogApp.urls')),
    path('about', include('blogApp.urls')),
    path('about_us', include('blogApp.urls')),
    path('contact_us', include('blogApp.urls')),
    path('post/contactus', include('blogApp.urls')),
    path('login', include('blogApp.urls')),
    path('logout', include('blogApp.urls')),
    path('post_delete', include('blogApp.urls')),
    path('create_post', include('blogApp.urls')),
    path('post/edit/<int:pk>', include('blogApp.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
