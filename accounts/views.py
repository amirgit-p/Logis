from django.shortcuts import render, redirect
from .forms import LoginForm, SignUpForm, ChangePasswordForm ,Editprofile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth import password_validation

def login_user(request):
    if request.method =='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("root:home")
            else:
                messages.add_message(request, messages.ERROR,"user not found")
                return redirect(request.path_info)

    else:
        return render(request,"registration/login.html")
@login_required
def logout_user(request):
    logout(request)
    return redirect("root:home")

def signup_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("root:home")
        else:
                messages.add_message(request, messages.ERROR, "Invalid input data")
                return redirect(request.path_info)
    else:
        return render(request, "registration/signup.html")

@login_required
def change_password(request):
    user = request.user
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            pass1 = form.cleaned_data['password1']
            pass2 = form.cleaned_data['password2']
            if (pass1 == pass2)and not (user.check_password(pass1)):
                try:
                    password_validation.validate_password(pass1)
                except:
                    messages.add_message(request, messages.ERROR, "Validation Failed")
                    return redirect(request.path_info)
                else:
                    user.set_password(pass1)
                    user.save
                    login(request,user)
                    messages.add_message(request, messages.SUCCESS, "Password has been changed successfully")
                    return redirect(request.path_info)
                
            else:
                messages.add_message(request, messages.ERROR, "Passwords Do Not Match OR Password is the old password")
                return redirect(request.path_info)
            
        else:
            messages.add_message(request, messages.ERROR, "Invalid Data")
            return redirect(request.path_info)   
    else:
        return render(request,"registration/change-password.html")

def reset_password(request):
    pass

def reset_password_done(request):
    pass
def reset_password_confirm(request):
    pass
def  reset_password_complete(request):
    pass

@login_required
def  edit_profile(request):
    user=request.user
    if request.method == 'POST' :
        form=Editprofile(request.POST,request.FILES,instance=user)
        if form.is_valid:
            form.save
            messages.add_message(request,messages.SUCCESS,"Profile updated successfully")
            return redirect("accounts:edit_profile")
        else:
             messages.add_message(request, messages.ERROR, "Invalid input data")
             return redirect("accounts:edit_profile")
    else:
        form=Editprofile(instance=user)
        context={
            "form":form,
        }
        return render(request,"registration/edit-profile.html",context=context)
