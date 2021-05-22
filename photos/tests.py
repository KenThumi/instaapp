from photos.models import Profile
from django.test import TestCase
from django.contrib.auth.models import User

class ProfileTestClass(TestCase):
    '''Test methods of profile model'''

    def setUp(self):
        self.user_1 = User.objects.create_user('Chevy Chase', 'chevy@chase.com', 'chevyspassword')
        self.profile=Profile(profile_photo='imageurl.png',bio='Lorem ipsum',user=self.user_1)

    
    def tearDown(self):
        self.user_1.delete()
        self.profile.delete()

    def test_save_profile(self):
        self.user_1.save()
        self.profile.save()

        profiles = Profile.objects.all()

        self.assertTrue(len(profiles)>0)