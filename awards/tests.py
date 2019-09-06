from django.test import TestCase
from django.models import profile, Projects
from django.contrib.auth.models import User

# Create your tests here.
class Project(TestCase):
    def test_is_instance(self):
        self.assertTrue(isinstance(self.project,projects))

    def test_save_method(self):
        """
        function that tests whether an image is saved to the database
        """

        projects = Projects.objects.all()

        self.save_project()




class Profile(TestCase):
    """
    testing profiles
    """

    def setUp(self):
        """
        This will add new profile before each test
        """
        self.new_user = User(username = "joy")
        self.new_user.save()

    def test_is_instance(self):
        self.assertTrue(isinstance(self.new_user.profile, Profile))