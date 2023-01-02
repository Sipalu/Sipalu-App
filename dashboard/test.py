from django.test import TestCase
from django.contrib.auth.models import User
from unittest.mock import Mock
from django.http import HttpResponseRedirect


from .views import login
class LoginTestCase(TestCase):
    def test_login_with_valid_credentials(self):
        # Set up test data
        uname = 'testuser'
        passwd = 'testpass'
        user = User.objects.create_user(username=uname, password=passwd)

        # Set up a mock request object
        request = Mock(method='POST', POST={'username': uname, 'password': passwd})

        # Call the login function
        result = login(request)

        # Verify that the function returns a redirect response
        self.assertIsInstance(result, HttpResponseRedirect)
        self.assertEqual(result.status_code, 302)

        # Verify that the user was logged in
        self.assertEqual(request.user, user)