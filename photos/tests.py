from photos.models import Image, Profile
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



class ImageTestClass(TestCase):
    '''Test methods of Image model'''

    def setUp(self):
        self.user_1 = User.objects.create_user('Chevy Chase', 'chevy@chase.com', 'chevyspassword')
        self.profile=Profile(profile_photo='imageurl.png',bio='Lorem ipsum',user=self.user_1)
        self.image=Image(image='newimageurl.png',name='Test Image',caption='Lorem ipsum',profile=self.profile)

    
    def tearDown(self):
        self.image.delete()
        self.profile.delete()
        self.user_1.delete()


    def test_save_image(self):
        self.user_1.save()
        self.profile.save()
        self.image.save()

        images = Image.objects.all()

        self.assertTrue(len(images)>0)

    
    def test_update_caption(self):
        self.user_1.save()
        self.profile.save()
        self.image.save()

        update_details = {'image':'newlink.png',
                               'name':'image_name',
                                'caption':'some image description',
                                'profile':self.user_1.profile,
                             }


        Image.update_caption(update_details, self.image.id)

        self.updated_image = Image.objects.get(pk = self.image.id) #get new updated image

        cloudinary_url_prefix = 'http://res.cloudinary.com/dtw9t2dom/image/upload/'

        self.assertEqual(self.updated_image.image.url, cloudinary_url_prefix+'newlink.png')



    def test_delete_image(self):
        self.user_1.save()
        self.profile.save()
        self.image.save()

        self.image2 = Image.objects.get(pk=self.image.id)



        self.image2.delete_image()

        images = Image.objects.all()

        self.assertTrue(images.count() == 0)


