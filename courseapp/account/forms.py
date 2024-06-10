from typing import Any
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.forms import widgets
from django.contrib import messages
from django import forms
from django.contrib.auth.forms import PasswordChangeForm

class LoginUserForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields["username"].widget = widgets.TextInput(attrs={"class": "form-control"})
        self.fields["password"].widget = widgets.PasswordInput (attrs={"class": "form-control"})
    
    def clean_username(self):
        username = self.cleaned_data.get("username")

        if username == "admin":
            messages.add_message(self.request, messages.SUCCESS, "Hoş geldin admin")

        return username
    
    # def confirm_login_allowed(self, user):
    #     if user.username.startswith("s"):
    #         raise forms.ValidationError("bu kullanıcı adı ile login olamazsınız")
        
class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    

class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'wide-form-field'
    
    # class NewUserForm(UserCreationForm):
    #     class Meta:
    #         model = User
    #         fields = ("username", "email",)