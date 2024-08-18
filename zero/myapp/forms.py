from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import KullaniciIcerik  # KullaniciIcerik modelini import ediyoruz

class ExtendedUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='E-posta')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class KullaniciIcerikForm(forms.ModelForm):
    class Meta:
        model = KullaniciIcerik  # Modeli doğru bir şekilde tanımlıyoruz
        fields = ['baslik', 'video', 'resim', 'metin']
