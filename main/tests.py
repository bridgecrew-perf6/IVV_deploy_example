from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User


class IndexAuthTest(TestCase):
    fixtures = [
        "test.json",
    ]

    def test_auth_protection(self):
        c = Client()
        response = c.get(reverse("index"), follow=True)
        url, status_code = response.redirect_chain[-1]
        self.assertIn(reverse("login"), url)


class IndexTest(TestCase):
    fixtures = [
        "test.json",
    ]

    def setUp(self):
        self.c = Client()
        user = User.objects.get(username="vasya")
        self.c.force_login(user)

    def test_index_opens(self):
        response = self.c.get(reverse("index"))
        self.assertEqual(response.status_code, 200)

    def test_index_context(self):
        response = self.c.get(reverse("index"))
        self.assertTrue("menu" in response.context)

class MapTest(TestCase):
    fixtures = [
        "test.json",
    ]

    def setUp(self):
        self.c = Client()
        user = User.objects.get(username="vasya")
        self.c.force_login(user)

    def test_map_opens(self):
        response = self.c.get(reverse("map"))
        self.assertEqual(response.status_code, 200)

class MenuTest(TestCase):
    fixtures = [
        "test.json",
    ]

    def setUp(self):
        self.c = Client()
        user = User.objects.get(username="vasya")
        self.c.force_login(user)

    def test_map_opens(self):
        response = self.c.get(reverse("menu"))
        self.assertEqual(response.status_code, 200)

    def test_menu_context(self):
        response = self.c.get(reverse("menu"))
        self.assertTrue("menu" in response.context)
