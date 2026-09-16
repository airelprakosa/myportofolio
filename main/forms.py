from django.forms import ModelForm, TextInput, Textarea
from main.models import Project

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