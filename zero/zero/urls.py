from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from myapp import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profil/', include('myapp.urls')),  # myapp/urls.py dosyasına yönlendirme
    path('register/', views.register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('', views.index_view, name='index'),
    path('logout/', views.logout_view, name='logout_view'),
]

# Media dosyalarını servis etmek için
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
