from django.shortcuts import render, redirect, get_object_or_404
from .models import Review

def index(request):
    reviews = Review.objects.all()
    return render(request, 'reviews/index.html', {'reviews': reviews})

def create_review(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        store = request.POST['store']
        rating = request.POST['rating']
        Review.objects.create(title=title, description=description, store=store, rating=rating)
        return redirect('index')
    return render(request, 'reviews/create_review.html')

def review_detail(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    return render(request, 'reviews/review_detail.html', {'review': review})

def edit_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    if request.method == 'POST':
        review.title = request.POST['title']
        review.description = request.POST['description']
        review.store = request.POST['store']
        review.rating = request.POST['rating']
        review.save()
        return redirect('review_detail', review_id=review.id)
    return render(request, 'reviews/edit_review.html', {'review': review})

def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    if request.method == 'POST':
        review.delete()
        return redirect('index')
    return render(request, 'reviews/delete_review.html', {'review': review})
