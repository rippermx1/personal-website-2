from django.urls import path
from . import views
from experiences import views as experience_views
from education import views as education_views
from skills import views as skill_views

urlpatterns = [
    path('', views.home, name=''),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('education/', education_views.education, name='education'),
    path('experience/', experience_views.experiences, name='experience'),
    path('skills/', skill_views.skills, name='skills')
]
