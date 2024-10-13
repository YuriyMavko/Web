from django.urls import path
from .views import index, create, delete_article

urlpatterns = [
    path('', index, name='index'),
    path('create/', create, name='create'),
    path('delete/<int:id>/', delete_article, name='delete_article'),
]
