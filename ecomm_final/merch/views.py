from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def product(request):
    return render(request, 'product.html')

def about(request):
    return render(request, 'about.html')

# Create your views here.
