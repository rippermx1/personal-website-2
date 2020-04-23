from django.shortcuts import render
from .models import Skill

# Create your views here.
def skills(request):
    tech_skills = Skill.objects.filter(category=1)
    soft_skills = Skill.objects.filter(category=2)
    context = {
        'tech_skills': tech_skills,
        'soft_skills': soft_skills
    }
    return render(request, 'skills/skills.html', context)
