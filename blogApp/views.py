from django.shortcuts import redirect, render
from django.http import HttpResponse, request
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Post
from blogApp.models import Contacts
from django.core.mail import send_mail
from django.conf import settings
from django.views.generic import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .forms import PostForm


def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists!')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists!')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request, 'Passwords do not match!')
            return redirect('register')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
    
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials!')
            return redirect('login')
    else:
        return render(request, 'login.html')



def logout(request):
    auth.logout(request)
    return redirect('/')


def contact_us(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        details = Contacts(name=name, email=email, phone=phone, message=message)
        details.save()

        send_mail(
            "Your Issue",
            f"Hi {name}, \nThanks for contacting us! We'll reach out to you shortly! \n\n Thanks,\nBlogSite",
            settings.EMAIL_HOST_USER,
            [f'{email}'],
            fail_silently=False)

        messages.info(request, 'Message Sent Successfully!')

    return render(request, 'contact_us.html')


def post(request, pk):
    posts = Post.objects.get(id=pk)
    return render(request, 'post.html', {'posts': posts})


def about(request):
    return render(request, 'about.html')


def about_us(request):
    return render(request, 'about.html')


def contactus(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        details = Contacts(name=name, email=email, phone=phone, message=message)
        details.save()

        send_mail(
            "Your Issue",
            f"Hi {name}, \nThanks for contacting us! We'll look at your issue and reach out to you shortly! \n\n Hope you have a great day!\nBlogSite",
            settings.EMAIL_HOST_USER,
            [f'{email}'],
            fail_silently=False)

        messages.info(request, 'Message Sent Successfully!')

    return render(request, 'contact_us.html')


'''def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        subtitle = request.POST.get('subtitle')
        blog_post = request.POST.get('post')
        author = request.POST.get('author')

        add_post = Post(title=title, subtitle=subtitle, post=blog_post, author=author)
        add_post.save()
        messages.info(request, 'Blog Post Added Successfully!')

        return redirect('/')

    return render(request, 'create_post.html')
'''


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'create_post.html'
    success_url = reverse_lazy('index')


def post_delete(request):
    return redirect('delete_post')


class UpdatePostView(UpdateView):
    model = Post
    template_name = 'edit_post.html'
    fields = ['title', 'subtitle', 'post']
    success_url = reverse_lazy('index')


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('index')