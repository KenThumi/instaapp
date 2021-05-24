from photos.models import Comment, Image, Profile
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


    def test_update_profile(self):
        self.user_1.save()
        self.profile.save()

        update_details = {'profile_photo':'newlink.png',
                               'bio':'new bio',
                                'user':self.user_1
                             }


        Profile.update_profile(update_details, self.profile.id)

        self.updated_profile= Profile.objects.get(pk = self.profile.id) #get new updated profile

        cloudinary_url_prefix = 'http://res.cloudinary.com/dtw9t2dom/image/upload/'

        self.assertEqual(self.updated_profile.profile_photo.url, cloudinary_url_prefix+'newlink.png')

    
    def test_delete_profile(self):
        self.user_1.save()
        self.profile.save()

        self.newprof = Profile.objects.get(pk=self.profile.id)

        self.newprof.delete_profile()

        self.assertTrue(len(Profile.objects.all()) == 0)



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




class TestCommentClass(TestCase):
    '''Test methods of Comment model'''

    def setUp(self):
        self.comment = Comment(comment='simple comment',image_id='1',user_id=1)

    
    def tearDown(self):
        self.comment.delete()


    def test_save_comment(self):
        self.comment.save_comment()

        self.assertTrue( len(Comment.objects.all()) > 0)


    def test_update_comment(self):
        self.comment.save_comment()

        update_details = {'comment':'new comment',}


        Comment.update_comment(update_details, self.comment.id)

        self.updated_comment= Comment.objects.get(pk = self.comment.id) #get new updated comment


        self.assertEqual(self.updated_comment.comment, 'new comment')


    def test_delete_comment(self):
        self.comment.save_comment()

        self.fetchedcomment = Comment.objects.get(pk=self.comment.id)

        self.fetchedcomment.delete_comment()

        self.assertTrue( len(Comment.objects.all()) == 0)


    
       



