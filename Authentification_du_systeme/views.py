from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from Authentification_du_systeme.forms import RegistrationForm, UserEditForm, ProfileEditForm
from django.contrib.auth.decorators import login_required
from .models import Profile, CustomUser
from django.contrib import messages

# Create your views here.

def login_view(request):
    
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['motDePass']
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
        #user_form = RegistrationForm(request.POST)

        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        email = request.POST.get('email')
        telephone = request.POST.get('telephone')
        motDePass = request.POST.get('motDePass')
        motDePassDeConfirmation = request.POST.get('motDePassDeConfirmation')

        if motDePass != motDePassDeConfirmation :

            messages.error(request, "Le mot de pass de confirmation ne correspond pas à votre mot de pass")

            return render(request, 'registration/register.html')
        
        else :

            new_user = CustomUser(email=email, nom=nom, prenom = prenom, telephone = telephone)
            new_user.save()
            new_user.set_password(motDePass)
            new_user.save()

            return redirect('home')

        #if user_form.is_valid() :
        #    new_user = user_form.save(commit=False)
        #    new_user.set_password(user_form.cleaned_data['password'])
        #    new_user.save()
        #    Profile.objects.create(user=new_user)
        #    return redirect('login_view')
        #else :
        #    return render(request,'registration/register.html')
    
    return render(request,'registration/register.html')


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
            






