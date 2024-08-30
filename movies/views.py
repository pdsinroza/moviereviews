from django.shortcuts import render,get_object_or_404,redirect
from .models import Email,Movie,Review
# Create your views here.
def home(request):
    email_id = request.GET.get('email')
    searchTerm = request.GET.get('searchMovie')
    if searchTerm:
        movies =Movie.objects.filter(title__icontains = searchTerm)
    else:
        movies = Movie.objects.all()
    if email_id:
        email = Email.objects.create(emailid=email_id)
        email.save()
        return render (request,'email.html',{'email':email_id})
    return render(request,'home.html',{'movies':movies})

def email(request):
    return render(request, 'email.html')

def detail(request, movie_id):
    movies = get_object_or_404(Movie,pk=movie_id)
    reviews = Review.objects.filter(movie=movies)
    return render(request,'detail.html',{'movies':movies,'reviews':reviews})

def createreview(request,movie_id):
    movies = get_object_or_404(Movie,pk=movie_id)
    if request.method == 'GET':
        return render(request,'createreview.html',{'movies':movies})
    else:
        myreview = request.POST.get('myreview')
        newReview = Review()
        newReview.text = myreview
        newReview.movie = movies
        newReview.user = request.user
        newReview.save()
        return redirect('detail',newReview.movie.id)
    
def updatereview(request,review_id):
    review = get_object_or_404(Review,pk=review_id,user=request.user)
    if request.method == 'GET':
        return render(request,'updatereview.html',{'review':review})
    else:
        review.text = request.POST.get('myreview')
        review.save()
        return redirect('detail',review.movie.id)
    
def deletereview(request,review_id):
    review = get_object_or_404(Review,pk=review_id,user=request.user)
    review.delete()
    return redirect('detail', review.movie.id)