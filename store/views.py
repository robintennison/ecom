from django.shortcuts import render
from .models import Product, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignUpForm
from django.shortcuts import get_object_or_404




def home(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'home.html', {
        'products': products,
        'categories': categories
    })

def about(request):
    return render(request, 'about.html')

def product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product.html', {'product':product})



def category(request, category):
    category_obj = get_object_or_404(Category, id=category)
    products = Product.objects.filter(category=category_obj)
    return render(request, 'category.html', {
        'products': products,
        'category': category_obj,
    })

    def __str__(self):
        return self.name

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in")
            return redirect('home')
        else:
            messages.success(request, "There was an error logging in")
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect('home')

def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have registered successfully")
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form':form})