from django.shortcuts import render,redirect
from .forms import RegisterForm, UserUpdateForm,ProfileUpdate,CustomPasswordChangeForm
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from blog.models import Post
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy


def register_user(request):
    if request.method == 'POST':
        form=RegisterForm(request.POST or None )
        if form.is_valid():
            user = form.save(commit=False)
            # username = form.cleaned_data['username']
            user.set_password(form.cleaned_data['password1'])
            user.save()
            messages.success(request, f'{user}, your registration has been completed successfully')
            login(request,user)
            return redirect('home')
        
    else:
        form=RegisterForm()
    context = {
        'title':'Register',
        'form' : form
    }
    return render(request, 'user/register.html',  context)

def login_user(request):
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            messages.error(request, ("You Have Been Logged In !!"))
            return redirect('home')
        else:
            messages.error(request, ("There was an error logging in. Please Try Again..."))
            return redirect('login')
        
    else: 
        context = {
            "title": "LogIn",
        }
        return render(request, 'user/login.html', context )
    
    
def logout_user(request):
    logout(request)
    context = {
        "title": "Logout",
    }
    return render(request , 'user/logout.html', context)


@login_required(login_url='login')
def profile(request):
    posts = Post.objects.filter(author=request.user)
    context = {
        "title": "Profile",
        'posts': posts,
    }
    return render(request , 'user/profile.html', context)


@login_required(login_url='login')
def updateprofile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance= request.user)
        profile_form = ProfileUpdate(request.POST,request.FILES, instance= request.user.profile)
        if user_form.is_valid and profile_form.is_valid:
            user_form.save()
            profile_form.save()
            messages.success(request, 'your profile is updated')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance= request.user)
        profile_form = ProfileUpdate(instance= request.user.profile)
            
        
    context = {
        'title' : 'ProfileUpdate',
        'user_form' : user_form,
        'profile_form' : profile_form,
    }
    return render(request , 'user/updateprofile.html', context)




class Passwordchangeview(PasswordChangeView):
    form_class = CustomPasswordChangeForm
    success_url = reverse_lazy('password_success')

    
def password_success(request):
    return render(request, "user/password_success.html")

