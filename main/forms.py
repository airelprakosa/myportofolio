from django.core.exceptions import ValidationError
from django.forms import ModelForm, TextInput, Textarea,Select, URLInput
from django.utils.html import strip_tags
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

    def clean_title(self):
        title = strip_tags(self.cleaned_data["title"]).strip()
        if not title:
            raise ValidationError("Nama proyek tidak boleh hanya berisi tag HTML.")
        return title

    def clean_category(self):
        return strip_tags(self.cleaned_data["category"]).strip()

    def clean_description(self):
        return strip_tags(self.cleaned_data["description"]).strip()
        
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

    def clean_title(self):
        title = strip_tags(self.cleaned_data["title"]).strip()
        if not title:
            raise ValidationError("Posisi / peran tidak boleh hanya berisi tag HTML.")
        return title

    def clean_description(self):
        description = strip_tags(self.cleaned_data["description"]).strip()
        if not description:
            raise ValidationError("Deskripsi tidak boleh hanya berisi tag HTML.")
        return description
