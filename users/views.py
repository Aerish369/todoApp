from django.shortcuts import render, redirect

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from .models import Profile
from django.contrib.auth.models import User


from django.contrib import messages


from .forms import CustomUserCreationForm


# Create your views here.
@login_required(login_url="user-login")
def userAccount(request):

    profile = request.user.profile
    context = {
        'profile': profile,
    }
    return render(request, 'users/account.html', context)


def userLogin(request):

    if request.user.is_authenticated:
        return redirect('tasks')

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request, "Username not found")
        
        user = authenticate(request, username= username, password = password)
        
        if user is not None:
            login(request, user)
            return redirect('tasks')
        else:
            messages.error(request, "Username or Password incorrect")

    return render(request, 'users/login.html')


def userLogout(request):
    logout(request)
    return redirect('user-login')


def userRegister(request):
    page = 'register'

    if request.user.is_authenticated:
        return redirect('tasks')
    
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            newProfile = form.save(commit=False)
            newProfile.username = newProfile.username.lower()
            newProfile.save()
            login(request, newProfile)

            messages.success(request, "User account created successfully!")

            return redirect('tasks')

    context = {
        'page':page,
        'form': form,
    }
    return render(request, 'users/login.html', context)