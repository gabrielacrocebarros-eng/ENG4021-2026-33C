"""
URL configuration for moviesproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from moviesapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home2, name='catalog'),
    path("users",view.create_user),
    path("users/login/",view.login_user, name="login"),
    path("users/logout/",view.logout_user, name="logout"),
    #path("users/",include("django.contrib.auth.urls")),
    path('filmes/novo/', movie_create, name='movie_create'),
    path('filmes/<int:pk>/editar/', movie_update, name='movie_update'),
    path('filmes/<int:pk>/excluir/', movie_delete, name='movie_delete'),
]
