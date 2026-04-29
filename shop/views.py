from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Product


def register_view(request):
    print("VIEW ENTERED")

    if request.method == "POST":
        print("POST RECEIVED")
        print("DATA:", request.POST)

        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm = request.POST.get('confirm_password')

        if not username or not password:
            messages.error(request, "Username va password kiritilishi shart ")
            return redirect('register')

        if password != confirm:
            print("PASSWORD NOT MATCH")
            messages.error(request, "Parollar mos emas ")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            print("USER EXISTS")
            messages.error(request, "Bunday user allaqachon bor iltimos boshqa username kiriting")
            return redirect('register')

        user = User.objects.create_user(username=username, password=password)

        print("USER CREATED:", user)

        messages.success(request, "Ro'yxatdan muvaffaqiyatli o'tdingiz ")
        return redirect('login')

    return render(request, 'register.html')
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        print("USERNAME:", username)
        print("PASSWORD:", password)

        user = authenticate(request, username=username, password=password)

        print("AUTH RESULT:", user)

        if user is not None:
            login(request, user)
            return redirect('products')
        else:
            messages.error(request, "Login yoki parol xato ")
            return redirect('login')

    return render(request, 'login.html')
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

@login_required
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_detail.html', {'product': product})

