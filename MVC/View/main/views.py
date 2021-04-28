from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import *
from .forms import *

# Create your views here.
def home(request):
    allMovies = Movie.objects.all() # select * from movie

    context = {
        "movies": allMovies,

    }

    return render(request, 'main/index.html', context)

# detail page
def detail(request, id):
    movie = Movie.objects.get(id=id)
    reviews = Review.objects.filter(movie=id).order_by("-comment")

    context = {
        "movie": movie,
        "reviews": reviews

    }
    return render(request, 'main/details.html', context)

# def main(request):
#     return render(request, 'base.html')

#add movies to the database
# def add_movies(request):
#     if request.method == "POST":
#         form = MovieForm(request.POST or None)

#         #check if form is valid:
#         if form.is_valid():
#             data = form.save(commit=False)
#             data.save()
#             return redirect("main:home")
#         else:
#             form = MovieForm()
#         return render(request, 'main/addmovies.html', {"form": form})

def add_movies(request):
    if request.user.is_authenticated:

        if request.user.is_superuser:
            submitted = False
            if request.method == "POST":
                form = MovieForm(request.POST)
                if form.is_valid():
                    form.save()
                    return HttpResponseRedirect('/addmovies?submitted=True')
            else:
                form = MovieForm
                if 'submitted' in request.GET:
                    submitted=True


            return render(request, 'main/addmovies.html', {"form": form, "controller": "Add Movie", 'submitted':submitted})
        #if they are not admin
        else:
            return redirect("main:home")
    #if they are not logged in
    else:
        return redirect("accounts:login")

def edit_movies(request, id):
    if request.user.is_authenticated:

        if request.user.is_superuser:
    # submitted = False
            movie = Movie.objects.get(id=id)

            if request.method == "POST":
                form = MovieForm(request.POST or None, instance=movie)

                if form.is_valid():
                    data = form.save(commit=False)
                    data.save()
                    return redirect("main:detail", id)
            else:
                form = MovieForm(instance=movie)
            # return HttpResponseRedirect('main/addmovies?submitted=True')
            return render(request, 'main/addmovies.html', {"form": form, "controller": "Edit Movie"})
         #if they are not admin
        else:
            return redirect("main:home")
    #if they are not logged in
    else:
        return redirect("accounts:login")

#delete movies
def delete_movies(request, id):
    if request.user.is_authenticated:

        if request.user.is_superuser:
            #get the movie
            movie = Movie.objects.get(id=id)

            #delete the movie
            movie.delete()
            return redirect("main:home")

         #if they are not admin
        else:
            return redirect("main:home")
    #if they are not logged in
    else:
        return redirect("accounts:login")


def add_review(request, id):
    if request.user.is_authenticated:
        movie = Movie.objects.get(id=id)
        if request.method == "POST":
            form = ReviewForm(request.POST or None)
            if form.is_valid():
                data = form.save(commit=False)
                data.comment = request.POST["comment"]
                data.rating = request.POST["rating"]
                data.user = request.user
                data.movie = movie
                data.save()
                return redirect("main:detail", id)
        else:
            form = ReviewForm()
        return render(request, 'main/details.html', {"form": form})
    else:
        return redirect("accounts:login")
