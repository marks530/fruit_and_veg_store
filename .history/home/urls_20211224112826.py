"""fruit_n_veg URL Configuration

"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
]
    """[path('admin/', admin.site.urls),
path('accounts/', include('allauth.urls')),]
    """