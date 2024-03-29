from django.http import HttpResponse
from django.shortcuts import render, redirect

from filmapp.forms import MovieForm
from filmapp.models import Movie


# Create your views here.
def index(request):
    movie=Movie.objects.all()
    context={
        'movie_list':movie

    }
    return render(request,'index.html',context)
def detail(request):
    movie = Movie.objects.all()
    context = {
        'movie_list': movie

    }

    return render(request,'detailed.html',context)
def add_movie(request):
    if request.method=="POST":
        name=request.POST.get('name',)
        desc = request.POST.get('desc',)
        year = request.POST.get('year',)
        image = request.FILES['image']
        movie=Movie(name=name,desc=desc,year=year,image=image)
        movie.save()
    return render(request,'add.html')

def update(request,id):
    movie=Movie.objects.get(id=id)
    form =MovieForm(request.POST or None, request.FILES,instance=movie)
    if form.is_valid():

        form.save()
        return  redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movie})
