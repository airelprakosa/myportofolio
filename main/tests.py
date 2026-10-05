from django.contrib.auth.models import Group, User
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
        # Halaman hanya berisi kerangka; datanya dimuat lewat AJAX.
        response = self.client.get(reverse("main:show_experience"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        self.assertContains(response, 'id="experience-grid"')
        self.assertNotContains(response, 'id="add-experience-modal"')

    def test_skills_page_extends_base(self):
        response = self.client.get(reverse("main:show_skills"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "base.html")
        self.assertContains(response, reverse("main:login"))

    def test_projects_page_is_skeleton(self):
        response = self.client.get(reverse("main:show_projects"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "projects.html")
        self.assertContains(response, 'id="grid"')

    def test_projects_api_with_data(self):
        response = self.client.get(reverse("main:get_projects_json"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()[0]["fields"]["title"], self.project.title)

    def test_projects_api_empty(self):
        Project.objects.all().delete()
        response = self.client.get(reverse("main:get_projects_json"))
        self.assertEqual(response.json(), [])


class ExperienceAjaxTest(TestCase):
    def setUp(self):
        self.owner = User.objects.create_superuser("owner", password="rahasia-12345")
        self.member = User.objects.create_user("member", password="rahasia-12345")
        self.editor = User.objects.create_user("editor", password="rahasia-12345")
        self.editor.groups.add(Group.objects.create(name="Editor"))
        self.experience = Experience.objects.create(
            title="Staff Ahli Video Production COMPFEST",
            description="Responsible for producing and editing creative video content.",
            category="volunteer",
        )
        self.experience.starred_by.add(self.member)
        self.valid_data = {
            "title": "Graphic Designer",
            "description": "Membuat materi publikasi.",
            "category": "freelance",
        }

    def test_api_is_public_and_contains_star_info(self):
        response = self.client.get(reverse("main:get_experiences_data"))
        self.assertEqual(response.status_code, 200)
        fields = response.json()[0]["fields"]
        self.assertEqual(fields["title"], self.experience.title)
        self.assertEqual(fields["star_count"], 1)
        self.assertFalse(fields["is_starred"])
        self.assertEqual(fields["starred_by_names"], "member")

    def test_api_marks_star_of_logged_in_user(self):
        self.client.force_login(self.member)
        response = self.client.get(reverse("main:get_experiences_data"))
        self.assertTrue(response.json()[0]["fields"]["is_starred"])

    def test_api_search_by_title(self):
        url = reverse("main:get_experiences_data")
        self.assertEqual(len(self.client.get(url, {"title": "compfest"}).json()), 1)
        self.assertEqual(self.client.get(url, {"title": "tidak ada"}).json(), [])

    def test_api_filter_by_category(self):
        url = reverse("main:get_experiences_data")
        self.assertEqual(len(self.client.get(url, {"category": "volunteer"}).json()), 1)
        self.assertEqual(self.client.get(url, {"category": "research"}).json(), [])
        # Nilai di luar pilihan model diabaikan.
        self.assertEqual(len(self.client.get(url, {"category": "ngawur"}).json()), 1)

    def test_star_ajax_requires_login(self):
        url = reverse("main:toggle_star_experience_ajax", args=[self.experience.id])
        self.assertEqual(self.client.post(url).status_code, 401)
        self.assertEqual(self.experience.starred_by.count(), 1)

    def test_star_ajax_toggles(self):
        url = reverse("main:toggle_star_experience_ajax", args=[self.experience.id])
        self.client.force_login(self.editor)
        result = self.client.post(url).json()
        self.assertTrue(result["is_starred"])
        self.assertEqual(result["star_count"], 2)
        result = self.client.post(url).json()
        self.assertFalse(result["is_starred"])
        self.assertEqual(result["starred_by_names"], "member")

    def test_create_ajax_rejects_get(self):
        self.client.force_login(self.owner)
        response = self.client.get(reverse("main:create_experience_ajax"))
        self.assertEqual(response.status_code, 405)

    def test_create_ajax_forbidden_for_non_owner(self):
        url = reverse("main:create_experience_ajax")
        self.assertEqual(self.client.post(url, self.valid_data).status_code, 403)
        for user in (self.member, self.editor):
            self.client.force_login(user)
            self.assertEqual(self.client.post(url, self.valid_data).status_code, 403)
        self.assertEqual(Experience.objects.count(), 1)

    def test_create_ajax_success_for_owner(self):
        self.client.force_login(self.owner)
        response = self.client.post(reverse("main:create_experience_ajax"), self.valid_data)
        self.assertEqual(response.status_code, 201)
        self.assertTrue(Experience.objects.filter(title="Graphic Designer").exists())

    def test_create_ajax_validation_error(self):
        self.client.force_login(self.owner)
        data = {**self.valid_data, "title": """<img src="x" onerror="alert('XSS!')">"""}
        response = self.client.post(reverse("main:create_experience_ajax"), data)
        self.assertEqual(response.status_code, 400)
        self.assertIn("title", response.json()["errors"])

    def test_create_ajax_strips_html_tags(self):
        self.client.force_login(self.owner)
        data = {**self.valid_data, "title": "Halo <b>dunia</b>"}
        self.client.post(reverse("main:create_experience_ajax"), data)
        self.assertTrue(Experience.objects.filter(title="Halo dunia").exists())

    def test_member_cannot_manage_experience(self):
        self.client.force_login(self.member)
        update_url = reverse("main:update_experience", args=[self.experience.id])
        delete_url = reverse("main:delete_experience", args=[self.experience.id])
        self.assertEqual(self.client.get(update_url).status_code, 403)
        self.assertEqual(self.client.get(reverse("main:create_experience")).status_code, 403)
        self.assertEqual(self.client.post(delete_url).status_code, 403)
        self.assertTrue(Experience.objects.filter(pk=self.experience.id).exists())

    def test_editor_can_update_but_not_create_or_delete(self):
        self.client.force_login(self.editor)
        update_url = reverse("main:update_experience", args=[self.experience.id])
        delete_url = reverse("main:delete_experience", args=[self.experience.id])
        self.assertEqual(self.client.get(update_url).status_code, 200)
        self.assertEqual(self.client.get(reverse("main:create_experience")).status_code, 403)
        self.assertEqual(self.client.get(reverse("main:create_project")).status_code, 403)
        self.assertEqual(self.client.post(delete_url).status_code, 403)
        self.assertTrue(Experience.objects.filter(pk=self.experience.id).exists())

    def test_json_endpoint_hides_user_ids(self):
        response = self.client.get(reverse("main:get_experiences_json"))
        self.assertEqual(response.json()[0]["fields"]["starred_by"], [["member"]])

    def test_modal_hidden_from_editor(self):
        self.client.force_login(self.editor)
        response = self.client.get(reverse("main:show_experience"))
        self.assertNotContains(response, 'id="add-experience-modal"')

    def test_modal_rendered_for_owner(self):
        self.client.force_login(self.owner)
        response = self.client.get(reverse("main:show_experience"))
        self.assertContains(response, 'id="add-experience-modal"')
