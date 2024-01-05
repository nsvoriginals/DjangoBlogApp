from pyexpat.errors import messages
from django.shortcuts import render, redirect
from .forms import UserForm, BlogForm,LoginForm
from django.contrib.auth import authenticate, login
from .models import Blog  # Import the Blog model if not already imported


def register_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user object
            login(request, user)  # Log in the user
            return redirect('login')  # Redirect to a success page after registration (replace with the appropriate URL)
    else:
        form = UserForm()

    return render(request, 'index.html', {'form': form})

def publish(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.save()
            return redirect('read')  # Redirect to the read page after successful blog creation
    else:
        form = BlogForm()

    return render(request, 'publish.html', {'form': form})


def read(request):
    # Fetch all blogs from the database and pass them to the template
    blogs = Blog.objects.all()
    return render(request, 'read.html', {'blogs': blogs})
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)

            if user:
                login(request, user)
                return redirect('read')  # Redirect to the read page after successful login
            else:
                # Handle authentication failure
                return redirect('login')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})