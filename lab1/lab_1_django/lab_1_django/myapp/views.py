from django.shortcuts import render

def page_one(request):
    return render(request, 'page_one.html')

def page_two(request):
    return render(request, 'page_two.html')