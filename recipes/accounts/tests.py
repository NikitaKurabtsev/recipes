from django.contrib.auth import get_user_model
from django.test import TestCase

User = get_user_model()

class CustomUserTests(TestCase):

    def test_create_user(self):
        user = User.objects.create_user(
            username = 'test',
            email = 'test@email.com',
            password = 'testpassword'
        )

        self.assertEqual(user.username, 'test')
        self.assertEqual(user.email, 'test@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        user = User.objects.create_superuser(
            username = 'test_superuser',
            email = 'test_superuser@email.com',
            password = 'testpassword'
        )

        self.assertEqual(user.username, 'test_superuser')
        self.assertEqual(user.email, 'test_superuser@email.com',)
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
