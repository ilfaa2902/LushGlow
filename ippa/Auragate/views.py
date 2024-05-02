from django.shortcuts import render
def home(request):
    return render(request,'home.html')
# Create your views here.
def about(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, 'contact.html')