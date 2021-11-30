from django.shortcuts import render

# Create your views here.

def root(request):
    return render(request,'root.html')

def home(request):
    return render(request, 'home.html')    

def about(request):
    return render(request, 'about.html')    

def services(request):
    return render(request, 'services.html')    
        
