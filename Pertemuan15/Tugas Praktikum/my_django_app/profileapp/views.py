from django.shortcuts import render

def home(request):
    return render(request, 'profileapp/home.html')

def about(request):
    return render(request, 'profileapp/about.html')

def gallery(request):
    return render(request, 'profileapp/gallery.html')
