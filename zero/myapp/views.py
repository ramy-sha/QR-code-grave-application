import os
import shutil
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from .forms import KullaniciIcerikForm, ExtendedUserCreationForm
from django.contrib.auth.decorators import login_required
from .models import KullaniciIcerik

from django.http import JsonResponse


def delete_profile_picture(request):
    print("Profil resmini silme görünümü çalıştı.")
    # Profil resmini silme işlemini gerçekleştirin
    if request.user.profile.profile_picture:
        print("Profil resmi bulundu, silme işlemi gerçekleştiriliyor.")
        request.user.profile.profile_picture.delete()  # Profil resmini silin
        return JsonResponse({'message': 'Profil resmi başarıyla silindi.'})
    else:
        print("Profil resmi bulunamadı.")
        return JsonResponse({'error': 'Profil resmi bulunamadı.'}, status=400)


def register_view(request):
    if request.method == 'POST':
        form = ExtendedUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profil')
        else:
            error_messages = form.errors.values()
            context = {'form': form, 'error_messages': error_messages}
            return render(request, 'register.html', context)
    else:
        form = ExtendedUserCreationForm()

    context = {'form': form}
    return render(request, 'register.html', context)


@login_required
def profil(request):
    icerikler = KullaniciIcerik.objects.filter(kullanici=request.user)

    if request.method == 'POST':
        form = KullaniciIcerikForm(request.POST, request.FILES)

        if form.is_valid():
            yeni_icerik = form.save(commit=False)
            yeni_icerik.kullanici = request.user
            yeni_icerik.save()
            return redirect('profil')
    else:
        form = KullaniciIcerikForm()

    context = {'form': form, 'icerikler': icerikler}
    return render(request, 'profil.html', context)

@login_required
def delete_icerik(request, icerik_id):
    icerik = get_object_or_404(KullaniciIcerik, id=icerik_id)

    if icerik.kullanici == request.user:
        icerik.delete()

    return redirect('profil')

@login_required
def profil_delete(request):
    if request.method == 'POST':
        icerikler = KullaniciIcerik.objects.filter(kullanici=request.user)

        # Medya dosyalarını ve boş klasörleri sil
        for icerik in icerikler:
            if icerik.video:
                dosya_yolu = os.path.join(settings.MEDIA_ROOT, str(icerik.video))
                os.remove(dosya_yolu)
            if icerik.resim:
                dosya_yolu = os.path.join(settings.MEDIA_ROOT, str(icerik.resim))
                os.remove(dosya_yolu)
            if icerik.icerik_dosya:
                dosya_yolu = os.path.join(settings.MEDIA_ROOT, str(icerik.icerik_dosya))
                os.remove(dosya_yolu)

        # Kullanıcıya ait bütün içerikleri sil
        icerikler.delete()

        # Kullanıcıyı sil
        request.user.delete()

        # Kullanıcıya ait medya klasörünü sil
        user_media_folder = os.path.join(settings.MEDIA_ROOT, request.user.username)
        if os.path.exists(user_media_folder):
            try:
                shutil.rmtree(user_media_folder)
                print(f"{user_media_folder} klasörü başarıyla silindi.")
            except Exception as e:
                print(f"Klasör silinemedi: {e}")

        return redirect('login')

@login_required
def edit_icerik(request, icerik_id):
    icerik = get_object_or_404(KullaniciIcerik, id=icerik_id, kullanici=request.user)

    if request.method == 'POST':
        form = KullaniciIcerikForm(request.POST, request.FILES, instance=icerik)
        if form.is_valid():
            form.save()
            return redirect('profil')
    else:
        form = KullaniciIcerikForm(instance=icerik)

    context = {'form': form, 'icerik': icerik}
    return render(request, 'edit_icerik.html', context)

def index_view(request):
    return render(request, 'index.html')

def logout_view(request):
    logout(request)
    return redirect('index')

from django.http import JsonResponse

import os

from django.contrib.auth.models import User

# Profil resminin kaydedilmesi ve ilişkilendirilmesi
from .models import Profile

def save_profile_picture(request):
    if request.method == 'POST' and request.FILES.get('profile_picture'):
        profile_picture = request.FILES['profile_picture']
        user = request.user
        user_folder = os.path.join(settings.MEDIA_ROOT, user.username)
        if not os.path.exists(user_folder):
            os.makedirs(user_folder)
        file_name = f"{user.username}_{profile_picture.name}"
        with open(os.path.join(user_folder, file_name), 'wb+') as destination:
            for chunk in profile_picture.chunks():
                destination.write(chunk)

        # Profil resmini kullanıcı profiline kaydet
        profile, created = Profile.objects.get_or_create(user=user)
        profile.profile_picture = os.path.join(user.username, file_name)
        profile.save()

        return JsonResponse({'message': 'Profil resmi başarıyla kaydedildi.'})
    else:
        return JsonResponse({'error': 'Dosya bulunamadı.'}, status=400)

@login_required
def edit_content(request):
    if request.method == 'POST':
        form = KullaniciIcerikForm(request.POST, request.FILES)

        if form.is_valid():
            yeni_icerik = form.save(commit=False)
            yeni_icerik.kullanici = request.user
            yeni_icerik.save()
            return redirect('profil')
    else:
        form = KullaniciIcerikForm()

    icerikler = KullaniciIcerik.objects.filter(kullanici=request.user)
    context = {'form': form, 'icerikler': icerikler}
    return render(request, 'edit_content.html', context)
