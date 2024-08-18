from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.profil, name='profil'),  # Kök URL'sini 'profil' fonksiyonuna yönlendir
    path('delete/<int:icerik_id>/', views.delete_icerik, name='delete_icerik'),  # İçerik silme için URL deseni
    path('delete/', views.profil_delete, name='profil_delete'),  # Profil silme için URL deseni
    path('logout/', views.logout_view, name='logout_view'),  # Logout URL deseni
    path('edit_content/', views.edit_content, name='edit_content'),
    path('profil/edit_icerik/<int:icerik_id>/', views.edit_icerik, name='edit_icerik'),
    path('save_profile_picture/', views.save_profile_picture, name='save_profile_picture'),
    path('delete_profile_picture/', views.delete_profile_picture, name='delete_profile_picture'),]
