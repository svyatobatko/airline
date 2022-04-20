from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase

from authentication.models import *
from authentication.serializers import UserSerializer, LoginSerializer


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


class UserSerializerTestCase(TestCase):
    def test_serializer_user_ok(self):
        user_1 = User.objects.create(username='User', email='user@us.er')
        user_2 = User.objects.create(username='User2', email='user2@us.er')
        user = UserSerializer([user_1, user_2], many=True).data
        expected_data = [
            {
                'email': 'user@us.er',
                'username': 'User',
                'token': user_1.token
            },
            {
                'email': 'user2@us.er',
                'username': 'User2',
                'token': user_2.token
            },
        ]
        self.assertEquals(expected_data, user)


class UserLoginSerializerTestCase(TestCase):

    def test_login_serializer_user_ok(self):
        user_login = User.objects.create(username='User3', email='user3@us.er', password='qwerasdf')
        user_login_data = LoginSerializer([user_login], many=True).data
        expected_data = [
            {
                'email': 'user3@us.er',
                'username': 'User3',
                'token': user_login.token
            },
        ]
        self.assertEquals(expected_data, user_login_data)
