from django.shortcuts import render
from main.models import Experience, Project

def show_main(request):
    context = {
        'name': 'Raden Stanislaus Airell P.S',
        'npm': '2506657251',
        'study_program': 'S1 Sistem Informasi',
        'bio': 'Second-Year Information Systems student at Universitas Indonesia | Marketings | Graphic Designer | Video Editing | interested in digital marketing | interested in System Analyst',
    }
    return render(request, "index.html", context)

def show_experience(request):
    context = {
        'name': 'Raden Stanislaus Airell P.S',
        'experience_list': Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def show_projects(request):
    context = {
        'name': 'Raden Stanislaus Airell P.S',
        'project_list': Project.objects.all(),
    }
    return render(request, "projects.html", context)

from main.models import Experience, Project, Skill

def show_skills(request):
    context = {
        'name': 'Raden Stanislaus Airell P.S',
        'skill_list': Skill.objects.all(),
    }
    return render(request, "skills.html", context)