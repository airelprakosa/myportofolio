from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from main.models import Experience, Project

class MainTest(TestCase):
    def setUp(self):
        self.experience = Experience.objects.create(
            title="Staff Ahli Video Production COMPFEST",
            description="Responsible for producing and editing creative video content.",
            category="volunteer"
        )
        self.project = Project.objects.create(
            title="Personal Portfolio Website",
            description="Website portofolio pribadi berbasis Django.",
            category="WEB DEVELOPMENT",
            is_completed=True
        )

    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")
        self.assertEqual(response.status_code, 404)

    def test_experience_model(self):
        self.assertEqual(str(self.experience), "Staff Ahli Video Production COMPFEST")
        self.assertEqual(self.experience.category, "volunteer")
        self.assertTrue(self.experience.is_ongoing)

    def test_experience_page(self):
        response = self.client.get(reverse("main:show_experience"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        self.assertContains(response, self.experience.title)

    def test_projects_page(self):
        response = self.client.get(reverse("main:show_projects"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "projects.html")
        self.assertContains(response, self.project.title)