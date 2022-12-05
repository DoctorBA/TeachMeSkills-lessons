from django.contrib import admin
from django.urls import path, include 
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('login/', views.LoginView.as_view(template_name='accounts/login.html'),
         name='login'), 
    path('logout/', views.LogoutView.as_view(template_name='accounts/login.html'),
         name='logout'),
    path('accounts/', include('accounts.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
