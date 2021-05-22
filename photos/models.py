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
    
    # user = models.ForeignKey('User',on_delete=models.CASCADE)#,null=True

    def save_profile(self):
        return self.save()


    def __str__(self):
        return f'Profile: {self.user}'