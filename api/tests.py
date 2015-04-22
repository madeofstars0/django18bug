from django.test import TestCase
from .models import User

# Create your tests here.
class UserTestCase(TestCase):

    def test_a_communication_options_dont_bleed_over(self):
        """ArrayField shouldn't bleed over to other instances"""

        user1 = User(first_name="Bob", last_name="Dole")
        self.assertEqual(user1.communication_options, [])
        user1.add_communication_option('test1')
        self.assertEqual(user1.communication_options, ['test1'])
        user1.save()

        user2 = User(first_name="George", last_name="Carlin")
        self.assertEqual(user2.communication_options, [])
        user2.add_communication_option('test2')
        self.assertEqual(user2.communication_options, ['test2'])
        user2.save()

    def test_b_communication_options(self):
        """ArrayField bleeds across tests"""

        user3 = User(first_name="Ben", last_name="Franklin")
        self.assertEqual(user3.communication_options, [])
        user3.add_communication_option('test3')
        self.assertEqual(user3.communication_options, ['test3'])
        user3.save()

    def test_c_setting_communication_options_directly_works(self):
        """
        When setting the communication_options directly doesn't cause problems.
        """

        user4 = User(first_name="Ann", last_name="Frank")
        user4.communication_options = ['test4']
        self.assertEqual(user4.communication_options, ['test4'])
        user4.save()