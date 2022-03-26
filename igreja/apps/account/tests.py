from django.contrib.auth import get_user_model
from django.test import TestCase


class UserCreateTest(TestCase):
    def test_create_user(self):
        email = "daconnas@gmail.com"

        User = get_user_model()
        user = User.objects.create_user(email=email, password="123")

        self.assertEqual(user.email, email)

        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
