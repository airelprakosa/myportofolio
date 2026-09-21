from django.forms import ModelForm, TextInput, Textarea,Select, URLInput
from main.models import Project, Experience

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            "title",
            "description",
            "category",
            "is_completed",
        ]
        labels = {
            "title": "Nama Proyek",
            "description": "Deskripsi Proyek",
            "category": "Kategori (misal: Web App, Figma)",
            "is_completed": "Apakah Proyek Sudah Selesai?",
        }
        widgets = {
            "title": TextInput(attrs={"placeholder": "Contoh: Portfolio Website", "maxlength": 255}),
            "description": Textarea(attrs={"placeholder": "Ceritakan proyekmu di sini...", "rows": 3}),
            "category": TextInput(attrs={"placeholder": "Contoh: Django, HTML, CSS"}),
        }
        
class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = [
            "title",
            "description",
            "category",
            "thumbnail",
        ]
        labels = {
            "title": "Posisi / Peran",
            "description": "Deskripsi Pengalaman",
            "category": "Jenis Pengalaman",
            "thumbnail": "URL Thumbnail (Opsional)",
        }
        widgets = {
            "title": TextInput(attrs={"placeholder": "Contoh: Web Developer Intern", "maxlength": 255}),
            "description": Textarea(attrs={"placeholder": "Ceritakan pengalamanmu di sini...", "rows": 3}),
            "category": Select(attrs={"class": "form-select"}),
            "thumbnail": URLInput(attrs={"placeholder": "Contoh: https://drive.google.com/..."}),
        }