from collections import UserDict
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from account.forms import LoginUserForm
from django.contrib import messages

def user_login(request):
    if request.user.is_authenticated and "next" in request.GET:
        return render(request, 'account/login.html', {'error_message': 'Yetkiniz yok.'})

    if request.method == 'POST':
        form = LoginUserForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password") 
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.add_message(request, messages.SUCCESS, "Giriş Başarılı")
                nextUrl = request.GET.get("next", None)
                if nextUrl is not None:
                    return redirect("index")
                else:
                    return redirect(nextUrl)
            else:
                return render(request, 'account/login.html', {"form":form})
        else:
            return render(request, 'account/login.html', {"form":form})
    else:
        form = LoginUserForm()
        return render(request, "account/login.html", {"form":form})

def user_register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]

        if password != repassword:
            return render(request, "account/register.html", 
            {
                "error": "Parola eşleşmiyor.",
                "username": username,
                "email": email
            })
        
        if User.objects.filter(username=username).exists():
            return render(request, "account/register.html", 
            {
                "error": "username kullanılıyor.",
                "username":username,
                "email": email,
            })
       
        if User.objects.filter(email=email).exists():
            return render(request, "account/register.html", 
            {
                "error": "email kullanılıyor.",
                "username":username,
                "email": email,
            })
        
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return redirect('user_login')
    else:
        return render(request, "account/register.html")

def user_logout(request):
    messages.add_message(request, messages.SUCCESS, "Çıkış başarılı")
    logout(request)
    return redirect("index")