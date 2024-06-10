from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from account.forms import LoginUserForm, NewUserForm, CustomPasswordChangeForm
from django.urls import reverse
from django.contrib.auth import update_session_auth_hash

def user_login(request):
    if request.user.is_authenticated:
        return redirect("index")

    if request.method == 'POST':
        form = LoginUserForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.add_message(request, messages.SUCCESS, "Giriş Başarılı")
                next_url = request.GET.get("next", None)
                if next_url:
                    return redirect(next_url)
                else:
                    return redirect("index")
            else:
                messages.add_message(request, messages.ERROR, "Geçersiz kullanıcı adı veya şifre.")
                return render(request, 'account/login.html', {"form": form})
        else:
            messages.add_message(request, messages.ERROR, "Formda hatalar var.")
            return render(request, 'account/login.html', {"form": form})
    else:
        form = LoginUserForm()
        return render(request, "account/login.html", {"form": form})

def user_register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.add_message(request, messages.SUCCESS, "Kayıt başarılı ve giriş yapıldı.")
                return redirect("index")
        else:
            messages.add_message(request, messages.ERROR, "Formda hatalar var.")
    else:
        form = NewUserForm()
        
    return render(request, "account/register.html", {"form": form})

def user_logout(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, "Çıkış başarılı")
    return redirect("index")

def change_password(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  
            messages.add_message(request, messages.SUCCESS, "Şifreniz başarıyla güncellendi.")
            return redirect("index")
        else:
            messages.add_message(request, messages.ERROR, "Lütfen formu doğru doldurun.")
            return render(request, "account/change-password.html", {"form": form})
    else:
        form = CustomPasswordChangeForm(request.user)
        return render(request, "account/change-password.html", {"form": form})



# from django.contrib import messages
# from django.shortcuts import redirect, render
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth.forms import UserCreationForm
# from account.forms import LoginUserForm
# from account.forms import NewUserForm
# from django.urls import reverse
# from django.contrib.auth.forms import PasswordChangeForm
# from django.contrib.auth import update_session_auth_hash

# def user_login(request):
#     if request.user.is_authenticated:
#         return redirect("index")

#     if request.method == 'POST':
#         form = LoginUserForm(request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get("username")
#             password = form.cleaned_data.get("password")
#             user = authenticate(request, username=username, password=password)

#             if user is not None:
#                 login(request, user)
#                 messages.add_message(request, messages.SUCCESS, "Giriş Başarılı")
#                 next_url = request.GET.get("next", None)
#                 if next_url:
#                     return redirect(next_url)
#                 else:
#                     return redirect("index")
#             else:
#                 messages.add_message(request, messages.ERROR, "Geçersiz kullanıcı adı veya şifre.")
#                 return render(request, 'account/login.html', {"form": form})
#         else:
#             messages.add_message(request, messages.ERROR, "Formda hatalar var.")
#             return render(request, 'account/login.html', {"form": form})
#     else:
#         form = LoginUserForm()
#         return render(request, "account/login.html", {"form": form})

# def user_register(request):
#     if request.method == 'POST':
#         form = NewUserForm(request.POST)

#         if form.is_valid():
#             form.save()

#             username = form.cleaned_data["username"]
#             password = form.cleaned_data["password1"]
#             user = authenticate(request, username=username, password=password)
#             login(request, user)
#                 # messages.add_message(request, messages.SUCCESS, "Kayıt başarılı ve giriş yapıldı.")
#             return redirect("index")
#         else:
#             form = NewUserForm()
#             # messages.add_message(request, messages.ERROR, "Formda hatalar var.")
#             return render(request, "account/register.html", {"form": form})

#     # else:
#     #     form = NewUserForm()
#     #     return render(request, "account/register.html", {"form": form})

# def change_password(request):
#     if request.method == 'POST':
#         form = PasswordChangeForm(request.user, request.POST)
#         if form.is_valid():
#             user = form.save()
#             update_session_auth_hash(request, user)  # Important for keeping the user logged in
#             messages.add_message(request, messages.SUCCESS, "Şifreniz başarıyla güncellendi.")
#             return redirect("index")
#         else:
#             messages.add_message(request, messages.ERROR, "Lütfen formu doğru doldurun.")
#             return render(request, "account/change-password.html", {"form": form})
#     else:
#         form = PasswordChangeForm(request.user)
#         return render(request, "account/change-password.html", {"form": form})

# def user_logout(request):
#     logout(request)
#     messages.add_message(request, messages.SUCCESS, "Çıkış başarılı")
#     return redirect("index")



# from collections import UserDict
# from urllib import request
# from django.contrib import messages
# from django.shortcuts import redirect, render
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import AuthenticationForm
# from account.forms import LoginUserForm
# from account.forms import NewUserForm
# from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm

# def user_login(request):
#     if request.user.is_authenticated and "next" in request.GET:
#         return render(request, 'account/login.html', {'error_message': 'Yetkiniz yok.'})

#     if request.method == 'POST':
#         form = LoginUserForm(request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get("username")
#             password = form.cleaned_data.get("password") 
#             user = authenticate(request, username=username, password=password)

#             if user is not None:
#                 login(request, user)
#                 messages.add_message(request, messages.SUCCESS, "Giriş Başarılı")
#                 nextUrl = request.GET.get("next", None)
#                 if nextUrl is not None:
#                     return redirect("index")
#                 else:
#                     return redirect(nextUrl)
#             else:
#                 return render(request, 'account/login.html', {"form":form})
#         else:
#             return render(request, 'account/login.html', {"form":form})
#     else:
#         form = LoginUserForm()
#         return render(request, "account/login.html", {"form":form})

# def user_register(request):
#     if request.method == 'POST':
#         form = NewUserForm(request.POST)
        
#         if form.is_valid():
#             form.save()

#             username = form.cleaned_data["username"]
#             password = form.cleaned_data["password1"]
#             user = authenticate(request, username=username, password=password)
#             login(request, user)
#             return redirect("index")
        
#         else:
#             return render(request, "account/register.html", {"form":form})

#     else:
#         form = NewUserForm()
#         return render(request, "account/register.html", {"form":form})
    
# # def change_password(request):
# #     form = PasswordChangeForm()
# #     return render(request, "account/change-password.html", {"form": form})
        
# def user_logout(request):
#     messages.add_message(request, messages.SUCCESS, "Çıkış başarılı")
#     logout(request)
#     return redirect("index")