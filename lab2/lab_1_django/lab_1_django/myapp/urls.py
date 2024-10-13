from django.urls import path
from . import views

urlpatterns = [
    path('', views.page_one, name='home'),
    path('page_one/', views.page_one, name='page_one'),
    path('page_two/', views.page_two, name='page_two'),
]