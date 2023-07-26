from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User, Category, Marque, Produit, code_serie
from django.forms import modelformset_factory


class SignupForm(UserCreationForm):
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'type': 'email',
                'autofocus': False
                   }
        )
    )
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'autofocus': True}
        )
    )
   
    class Meta:
        model = User
        fields = ('username','email','password1','password2')

class CategoryForm(forms.ModelForm):
    nom = forms.CharField(
        widget=forms.TextInput(
            attrs={'autofocus': True}
        )
    )
    class Meta:
        model = Category
        fields = ['nom']
class marqueForm(forms.ModelForm):
    nom = forms.CharField(
        widget=forms.TextInput(
            attrs={'autofocus': True}
        )
    )
    class Meta:
        model = Marque
        fields = ['nom']

class produitForm(forms.ModelForm):
    num = forms.CharField(
        widget=forms.TextInput(
            attrs={'autofocus': True}
        )
    )
    nom = forms.CharField(
        widget=forms.TextInput(
            attrs={'autofocus': True}
        )
    )
    marque= forms.ModelChoiceField(queryset=Marque.objects.all())
    categorie= forms.ModelChoiceField(queryset=Category.objects.all())
    class Meta:
        model = Produit
        fields = ['num', 'nom','marque','categorie']

class codeForm(forms.ModelForm):
    code = forms.IntegerField(
        widget=forms.TextInput(
            attrs={'autofocus': True}
        )
    )
    produit= forms.ModelChoiceField(queryset=Produit.objects.all())
    class Meta:
        model = code_serie
        fields = ['code','produit']
