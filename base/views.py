from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'base/about.html')

def contact(request):
    return render(request, 'base/contact.html')

def about(request):
    return render(request, 'base/about.html')

def education(request):
    return render(request, 'base/education.html')

def experience(request):
    return render(request, 'base/experience.html')

def skills(request):
    return render(request, 'base/skills.html')