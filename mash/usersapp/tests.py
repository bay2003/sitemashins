from django.test import TestCase
from django.contrib.auth import get_user_model

class BlogUserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Создаем тестового пользователя
        BlogUser = get_user_model()
        cls.user = BlogUser.objects.create_user(username='testuser', email='test@example.com', password='testpassword')

    def test_email_field_unique(self):
        # Проверяем, что поле email является уникальным
        user = get_user_model().objects.create_user(username='testuser2', email='test@example.com', password='testpassword')
        self.assertRaises(Exception, user.save)

    def test_is_author_default_false(self):
        # Проверяем, что по умолчанию is_author равен False
        user = get_user_model().objects.create_user(username='testuser3', email='test3@example.com', password='testpassword')
        self.assertFalse(user.is_author)
from django.test import TestCase

# Create your tests here.
