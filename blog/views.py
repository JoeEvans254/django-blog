from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm , BlogForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Blog
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.contrib.auth import logout
from django.views.decorators.http import require_POST

def home(request):
    return render(request, 'blog/home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'blog/register.html', {'form': form})

@login_required
def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('home')
    else:
        form = BlogForm()
    return render(request, 'blog/create_blog.html', {'form': form})

def blog_list(request):
    query = request.GET.get("q")
    sort = request.GET.get("sort", "-created_at")  # Default: newest first

    blogs = Blog.objects.all()

    if query:
        blogs = blogs.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )

    if sort == "author":
        blogs = blogs.order_by("author__username")
    else:
        blogs = blogs.order_by(sort)

    return render(request, 'blog/blog_list.html', {'blogs': blogs})

def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    return render(request, 'blog/blog_detail.html', {'blog': blog})


@require_POST
def logout_view(request):
    logout(request)
    return redirect('home')  


