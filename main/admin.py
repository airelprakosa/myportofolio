from django.contrib import admin
from .models import Experience, Project  # Tambahkan Education ke sini kalau lu punya model Education

admin.site.register(Experience)
admin.site.register(Project)