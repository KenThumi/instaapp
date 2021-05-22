from django.db import models
from cloudinary.models import CloudinaryField

class Profile(models.Model):
    profile_photo = CloudinaryField('image')
    bio = models.TextField()
    user = models.OneToOneField(
                'User',
                on_delete=models.CASCADE,
            )
    
    # user = models.ForeignKey('User',on_delete=models.CASCADE)#,null=True


    def __str__(self):
        return f'Profile: {self.user}'