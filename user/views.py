from django.shortcuts import render,redirect
from user.forms import UserRegisterForm,ProfileUpdateForm,UserUpdateFomr
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.


def Register_View(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username} successfully')
            return redirect('login')
        else:
            username=form.cleaned_data.get('username')
            messages.warning(request,f'Account for {username}not created ')
            return redirect('register')
    else:
        form = UserRegisterForm()
        context= {
            "form": form
        }
        return render(request,'user/register.html',context)

@login_required()
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateFomr(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES,
                                   instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form= UserUpdateFomr(instance=request.user)
        p_form= ProfileUpdateForm(instance=request.user)

        context={
            "u_form": u_form,
            "p_form": p_form
        }

        return render(request,'user/profile.html',context)
