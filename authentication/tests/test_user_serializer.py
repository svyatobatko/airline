from django.test import TestCase

from authentication.models import *
from authentication.serializers import UserSerializer, LoginSerializer


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
