from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from Authentification_du_systeme.forms import  UserEditForm, ProfileEditForm
from django.contrib.auth.decorators import login_required
from .models import Profile, CustomUser
from django.contrib import messages
from shop.models import Commande
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver


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


def register_view(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        email = request.POST.get('email')
        telephone = request.POST.get('telephone')
        motDePass = request.POST.get('motDePass')
        motDePassDeConfirmation = request.POST.get('motDePassDeConfirmation')

        if not nom or not prenom or not email or not telephone or not motDePass or not motDePassDeConfirmation:
            messages.error(request, "Tous les champs doivent être remplis.")
            return render(request, 'registration/register.html')

        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Cet email a déjà été utilisé, veuillez entrer un autre.")
            return render(request, 'registration/register.html')
            
        if CustomUser.objects.filter(telephone=telephone).exists():
            messages.error(request, "Ce numéro de téléphone a déjà été utilisé, veuillez entrer un autre.")
            return render(request, 'registration/register.html')

        if motDePass != motDePassDeConfirmation:
            messages.error(request, "Le mot de passe de confirmation ne correspond pas au mot de passe entré.")
            return render(request, 'registration/register.html')

        new_user = CustomUser(email=email, nom=nom, prenom=prenom, telephone=telephone)
        new_user.set_password(motDePass)
        new_user.save()  

        messages.success(request, "Inscription réussie ! Vous pouvez vous connecter.")
        return redirect('login_view')

    return render(request, 'registration/register.html')


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)



@login_required(login_url='login_view')
def profile_view(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = None 

    context = {
        'profile': profile,
        'commandes': Commande.objects.filter(email=request.user.email),
    }
    return render(request, 'profile/profile.html', context)


@login_required(login_url='login_view')
def edit_profile(request):
    if request.method == "POST":
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()  
            profile_form.save()
            return redirect('profile') 

    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    return render(request, 'profile/edit.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
            






