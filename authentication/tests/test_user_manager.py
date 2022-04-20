from django.test import TestCase

from authentication.models import UserManager, User


class UserTest(TestCase):

    def test_create_user_with_all_fields(self):
        user_new = User.objects.create_user(username='user', email='user@us.er', password='qwerasdf')
        self.assertEquals(str(user_new), 'user@us.er')

    def test_create_user_without_email(self):
        user_new = User.objects.create_user(username='user', email='', password='qwerasdf')
        full_name = str(user_new.get_full_name)
        self.assertEquals(full_name, '<bound method User.get_full_name of <User: >>')

    def test_create_user_without_name(self):
        user_new = User.objects.create_user(username='', email='user@us.er', password='qwerasdf')
        short_name = str(user_new.get_short_name)
        self.assertEquals(short_name, '<bound method User.get_short_name of <User: user@us.er>>')

    def test_create_user_with_none_username(self):
        with self.assertRaises(TypeError) as context:
            UserManager().create_user(username=None, email='user@us.er', password='qwerasdf')

        error_msg = 'Users must have a username.'
        self.assertRaises(TypeError)
        self.assertEquals(str(context.exception), error_msg)

    def test_create_user_with_none_email(self):
        with self.assertRaises(TypeError) as context:
            UserManager().create_user(username='user', email=None, password='qwerasdf')

        error_msg = 'Users must have an email address.'
        self.assertRaises(TypeError)
        self.assertEquals(str(context.exception), error_msg)

    def test_create_super_user_with_all_fields(self):
        user_new = User.objects.create_superuser(username='user', email='user@us.er', password='qwerasdf')
        self.assertEquals(str(user_new), 'user@us.er')

    def test_create_super_user_with_none_password(self):
        with self.assertRaises(TypeError) as context:
            UserManager().create_superuser(username='user', email='user@us.er', password=None)

        error_msg = 'Superusers must have a password.'
        self.assertRaises(TypeError)
        self.assertEquals(str(context.exception), error_msg)
