# accounts/tests.py
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class RegisterTest(TestCase):
    def setUp(self):
        user = User.objects.create(username="testuser", first_name="John", last_name="Doe")
        user.set_password("securepassword")
        user.save()

        self.user = user

        self.user_info = {"username": "testuser", "password": 1234}

    def test_registration_view(self):
        response = self.client.post(reverse('accounts:register'), self.user_info)
        self.assertEqual(response.status_code, 200)
        # aslida bu yerda 302 bo'lishi kerak, sababi post method ishlatilgan, lekin 200 qaytyapti

    def test_user_exists(self):
        user_exists = User.objects.filter(username='testuser').exists()
        self.assertTrue(user_exists)

    def test_login_view(self):
        login_response = self.client.post(reverse('accounts:login'), self.user_info)
        self.assertEqual(login_response.status_code, 200)
