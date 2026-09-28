from django.urls import path
from main.views import (
    show_main, show_experience, show_projects, show_skills, 
    create_project, get_projects_json, delete_project,
    create_experience, update_experience, delete_experience, 
    get_experiences_json, get_experiences_xml, get_experiences_json_by_id, get_experiences_xml_by_id,
    register, login_user, logout_user,toggle_star
)

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    
    # routing experience
    path('experience/', show_experience, name='show_experience'),
    path('experience/add/', create_experience, name='create_experience'),
    path('experience/<uuid:experience_id>/edit/', update_experience, name='update_experience'),
    path('experience/<uuid:experience_id>/delete/', delete_experience, name='delete_experience'),
    
    # routing project
    path('projects/', show_projects, name='show_projects'),
    path('projects/add/', create_project, name='create_project'),
    path('api/projects/', get_projects_json, name='get_projects_json'),
    path('projects/<int:project_id>/delete/', delete_project, name='delete_project'),
    
    # routing skills
    path('skills/', show_skills, name='show_skills'),
    
    # Endpoint Data Delivery Experience
    path('xml/experiences/', get_experiences_xml, name='get_experiences_xml'),
    path('json/experiences/', get_experiences_json, name='get_experiences_json'),
    path('xml/experiences/<uuid:experience_id>/', get_experiences_xml_by_id, name='get_experiences_xml_by_id'),
    path('json/experiences/<uuid:experience_id>/', get_experiences_json_by_id, name='get_experiences_json_by_id'),

    #register, login, logout
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path("projects/<int:project_id>/star/", toggle_star, name="toggle_star"),
]