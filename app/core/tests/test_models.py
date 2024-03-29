from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_sucessful(self):
        """测试用户，包含邮件"""
        email='test@gmail.com'
        password='Testpass123'
        user=get_user_model().object.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        email="test@gmail.com"
        user = get_user_model().object.create_user(email,'tet123')

        self.assertEqual(user.email,email.lower())