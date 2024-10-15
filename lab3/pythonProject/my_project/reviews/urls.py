from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_review, name='create_review'),
    path('review/<int:review_id>/', views.review_detail, name='review_detail'),
    path('review/<int:review_id>/edit/', views.edit_review, name='edit_review'),
    path('review/<int:review_id>/delete/', views.delete_review, name='delete_review'),
]
