import os
from django.db import models
from django.contrib.auth.models import User


def kullanici_dosya_yolu(instance, filename):
    # Dosya uzantısını al
    dosya_uzantisi = filename.split('.')[-1]
    # Kullanıcının adını ve dosya adını birleştirerek yeni bir dosya adı oluştur
    yeni_dosya_adı = f"{instance.kullanici.username}/{filename}"
    # Yeni dosya adını döndür
    return yeni_dosya_adı

class KullaniciIcerik(models.Model):
    kullanici = models.ForeignKey(User, on_delete=models.CASCADE)
    baslik = models.CharField(max_length=255)
    video = models.FileField(upload_to=kullanici_dosya_yolu, null=True, blank=True)
    resim = models.ImageField(upload_to=kullanici_dosya_yolu, null=True, blank=True)
    metin = models.TextField(null=True, blank=True)
    icerik_dosya = models.FileField(upload_to=kullanici_dosya_yolu, null=True, blank=True)
    tarih = models.DateTimeField(auto_now_add=True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
