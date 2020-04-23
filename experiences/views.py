from django.shortcuts import render
from .models import Experience

# Create your views here.
def experiences(request):
    experiences = Experience.objects.all()
    return render(request, 'experiences/experience.html', {'experiences': experiences})