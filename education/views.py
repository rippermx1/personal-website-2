from django.shortcuts import render
from .models import Education

# Create your views here.
def education(request):
    educationals = Education.objects.all()
    return render(request, 'education/education.html', {'educationals': educationals})