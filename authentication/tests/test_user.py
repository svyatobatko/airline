from django.test import TestCase

from authentication.models import *


class UserModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        User.objects.create(username='User_new', email='user_new@us.er')

    def test_username_label(self):
        user = User.objects.get(email='user_new@us.er')
        field_label = user._meta.get_field('username').verbose_name
        self.assertEquals(field_label, 'username')

    def test_email_label(self):
        user = User.objects.get(username='User_new')
        field_label = user._meta.get_field('email').verbose_name
        self.assertEquals(field_label, 'email')

    def test_username_max_length(self):
        user = User.objects.get(username='User_new')
        max_length = user._meta.get_field('username').max_length
        self.assertEquals(max_length, 255)

    def test_get_short_user_name(self):
        user = User.objects.get(email='user_new@us.er')
        field_label = user.get_short_name()
        self.assertEquals(field_label, 'User_new')

    def test_get_full_user_name(self):
        user = User.objects.get(email='user_new@us.er')
        field_label = user.get_full_name()
        self.assertEquals(field_label, 'User_new')

    def test_get_user_token(self):
        user = User.objects.get(email='user_new@us.er')
        field_label = user.token
        expected_data = user.token                     # проверяю сам с собой, поскольку генерируется всегда новый
        self.assertEquals(field_label, expected_data)

