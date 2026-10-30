from django.shortcuts import get_object_or_404, redirect, render
from .forms import MovieForm
from .models import Movie import requests
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, authenticate, logout
from django.contrib.auth.decorators import login_required


@login_required
def home2(request):
    movies = Movie.objects.all()
    return render(request, 'home.html', {'movies': movies})

@login_required
def movie_create(request):
    form = MovieForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('catalog')
    return render(request, 'movie_form.html', {'form': form, 'page_title': 'Novo filme'})

@login_required
def movie_update(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    form = MovieForm(request.POST or None, instance=movie)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('catalog')
    return render(request, 'movie_form.html', {'form': form, 'page_title': 'Atualizar filme'})

@login_required
def movie_delete(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        movie.delete()
        return redirect('catalog')
    return render(request, 'movie_confirm_delete.html', {'movie': movie})

def home(request):
    response = requests.get('https://omdbapi.com/?apikey=38b4b85b&s=Batman&type=movie')
    results_json=response.json()
    movies=results_json.get['Search']
    context = {
        'movies': movies
    }
    return render(request, 'index.html', context) 

def create_user(request):
    if request.method == 'POST':
        user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
        user.save()
        return redirect('home')
    return render(request,"register.html",context={"action":"Adicionar"})

def login_user(request):
    if request.method == 'POST':
    user = authenticate(username=request.POST['username'],password=request.POST['password'])
    if user!= None:
      login(request, user)
    else:
        return render(request,"login.html",context={"error_msg":"Usuário não existe"})

    if request.user.is_authenticated:
        return redirect('home')
    return render(request,"login.html",context={"error_msg":"Usuário não pode ser logado"})

def logout_user(request):
    logout(request)
    return redirect('login')