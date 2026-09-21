from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from main.models import Experience, Project, Skill
from main.forms import ProjectForm,ExperienceForm

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
    json_response = get_projects_json(request)
    projects = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    projects = [project.object for project in projects]
    title_query = request.GET.get("title", "").strip()
    context = {
        "name": "Raden Stanislaus Airell P.S",
        "project_list": projects,
        "title_query": title_query,
    }
    return render(request, "projects.html", context)

def show_skills(request):
    context = {
        'name': 'Raden Stanislaus Airell P.S',
        'skill_list': Skill.objects.all(),
    }
    return render(request, "skills.html", context)

def create_project(request):
    form = ProjectForm(request.POST or None)
    
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek baru berhasil ditambahkan!")
        return redirect("main:show_projects")
        
    context = {
        "name": "Raden Stanislaus Airell P.S",
        "form": form,
    }
    return render(request, "projects_form.html", context)

def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.all()
    if title_query:
        projects = projects.filter(title__icontains=title_query)
    projects_json = serializers.serialize("json", projects)
    return HttpResponse(projects_json, content_type="application/json")

def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
        return redirect("main:show_projects")
    return redirect("main:show_projects")

def get_experiences_json(request):
    experiences = Experience.objects.all()
    experiences_json = serializers.serialize("json", experiences)
    return HttpResponse(experiences_json, content_type="application/json")

def create_experience(request):
    form = ExperienceForm(request.POST or None)
    
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Pengalaman baru berhasil ditambahkan!")
        return redirect("main:show_experience")
        
    context = {
        "name": "Raden Stanislaus Airell P.S",
        "form": form,
    }
    return render(request, "experience_form.html", context)

def update_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)
    form = ExperienceForm(request.POST or None, instance=experience)
    
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Pengalaman berhasil diperbarui!")
        return redirect("main:show_experience")
        
    context = {
        "name": "Raden Stanislaus Airell P.S",
        "form": form,
        "experience_id": experience_id,
    }
    return render(request, "experience_form.html", context)

def delete_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)
    if request.method == "POST":
        experience.delete()
        messages.success(request, "Pengalaman berhasil dihapus!")
        return redirect("main:show_experience")
    return redirect("main:show_experience")

def get_experiences_xml(request):
    experiences = Experience.objects.all()
    return HttpResponse(serializers.serialize("xml", experiences), content_type="application/xml")

def get_experiences_json_by_id(request, experience_id):
    experience = Experience.objects.filter(pk=experience_id)
    return HttpResponse(serializers.serialize("json", experience), content_type="application/json")

def get_experiences_xml_by_id(request, experience_id):
    experience = Experience.objects.filter(pk=experience_id)
    return HttpResponse(serializers.serialize("xml", experience), content_type="application/xml")