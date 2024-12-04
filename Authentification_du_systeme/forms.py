from django import forms
from .models import CustomUser, Profile
from django.contrib.auth.forms import UserCreationForm



class RegistrationForm(forms.ModelForm) :

#    username = forms.CharField(label="Nom d'utilisateur", max_length=200, help_text='', required=True, min_length=5, widget=forms.TextInput(attrs={"class":"form-control", "id":"nomDutilisateur", "type":"text", "placeholder":"Nom d'utilisateur", "data-sb-validations":"required" }))
    first_name = forms.CharField(label="Nom", max_length=200, help_text='', required=True, min_length=5, widget=forms.TextInput(attrs={"class":"form-control", "id":"nom", "type":"text", "placeholder":"Nom", "data-sb-validations":"required, nom" }))
    last_name = forms.CharField(label="Prénom", max_length=200, help_text='', required=True, min_length=5, widget=forms.TextInput(attrs={"class":"form-control", "id":"prenom", "type":"text", "placeholder":"Prenom", "data-sb-validations":"required,prenom" }))
    email = forms.EmailField(label="Email", max_length=200, help_text='', required=True,min_length=5, widget=forms.TextInput(attrs={"class":"form-control", "id":"email", "type":"email", "placeholder":"Email", "data-sb-validations":"required,email" }))
    telephone = forms.CharField(label="Numéro de téléphone", max_length=200, help_text='', required=True, min_length=9, widget=forms.TextInput(attrs={"class":"form-control", "id":"telephone", "type":"number", "placeholder":"Numéro de téléphone", "data-sb-validations":"required, telephone" }))
    password = forms.CharField(label="Mot de pass", max_length=20, help_text='', required=True, min_length=8, widget=forms.TextInput(attrs={"class":"form-control", "id":"motDePass", "type":"password", "placeholder":"Mot de pass", "data-sb-validations":"required" }))
    confirm_password = forms.CharField(label="Mot de pass", max_length=20, help_text='', required=True, min_length=8, widget=forms.TextInput(attrs={"class":"form-control", "id":"motDePassDeConfirmation", "type":"password", "placeholder":"Mot de pass de confirmation", "data-sb-validations":"required" }))  

    class Meta :

        model = CustomUser
        fields = ('first_name',)




class UserEditForm(forms.ModelForm) :

    class Meta :
        model = CustomUser
        fields = ['email','password']


class ProfileEditForm(forms.ModelForm) :

    class Meta :
        model = Profile
        fields = ['birthday', 'profile_image', 'bio']
