from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from Authentification_du_systeme.forms import RegistrationForm, UserEditForm, ProfileEditForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib import messages

# Create your views here.

def login_view(request):
    
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  
        else:
            messages.error(request, 'Email ou mot de passe incorrect.')
            return render(request, 'registration/login.html')
    return render(request, 'registration/login.html')

    


def logout_view(request) :

    logout(request)
    return redirect('home')


def register_view(request) :

    if request.method == 'POST' :
        user_form = RegistrationForm(request.POST)

        if user_form.is_valid() :
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return redirect('login_view')
        else :
            return render(request,'registration/register.html', {'user_form':user_form})
    else :
        user_form = RegistrationForm()
    return render(request,'registration/register.html', {'user_form':user_form})


@login_required
def dashboard (request) :
    user = Profile.objects.filter(user=request.user).first()
    return render(request, 'profile/dashboard.html', {'user':user})


@login_required
def edit_profile(request) :
    if request.method == "POST" :
        user_form = UserEditForm(instance=request.user, data=request.POST,)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid() :
            user_form.save
            profile_form.save()
            return redirect('dashboard')

    else :
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request, 'profile/edit.html', {'user_form' : user_form, 
                                              'profile_form':profile_form})
            






