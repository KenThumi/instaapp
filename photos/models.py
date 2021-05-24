from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

class Profile(models.Model):
    profile_photo = CloudinaryField('image')
    bio = models.TextField()
    user = models.OneToOneField(
                User,
                on_delete=models.CASCADE,
            )

    def save_profile(self):
        return self.save()


    @classmethod
    def update_profile(cls,update_details,id):
        return cls.objects.filter(id=int(id)).update(profile_photo=update_details['profile_photo'],
                                               bio=update_details['bio'],
                                               user=update_details['user'])

    def delete_profile(self):
        return self.delete()


    def __str__(self):
        return f'Profile: {self.user.username}'


class Image(models.Model):

    image = CloudinaryField('image')
    name = models.CharField(max_length=60)
    caption = models.TextField()
    profile = models.ForeignKey('Profile',on_delete=models.CASCADE,related_name='images')
    likes = models.IntegerField(null=True)
    


    def save_image(self):
        return self.save()
       

    @classmethod
    def update_caption(cls,update_details,id):
        return cls.objects.filter(id=int(id)).update(image=update_details['image'],
                                               name=update_details['name'],
                                               caption=update_details['caption'],
                                               profile=update_details['profile'])
    


    def delete_image(self):
        return self.delete()

    class Meta:
        ordering = ["-pk"]

    def __str__(self):
        return f'Image: {self.name}'



class Comment(models.Model):
    comment = models.TextField()
    image = models.ForeignKey('Image', on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='comments')
    created = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ["-pk"]


    def save_comment(self):
        return self.save()

    
    @classmethod
    def update_comment(cls,update_details,id):
        return cls.objects.filter(id=int(id)).update(comment=update_details['comment'])


    def delete_comment(self):
        return self.delete()



    def __str__(self):
        return f'{self.user.user.username} Comment on {self.image.name}'


