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

    # @property
    # def isOwner(self,re):
    #     # print(request.user.id)
    #     print(self.request.user.id)
    #     return self.profile.user.id == request.user.id
       


    @classmethod
    def update_caption(cls,update_details,id):
        return cls.objects.filter(id=int(id)).update(image=update_details['image'],
                                               name=update_details['name'],
                                               caption=update_details['caption'],
                                               profile=update_details['profile'])
    
    # @classmethod
    # def search_category(cls,category):
    #     try:
    #         #results = cls.objects.get(category__name__icontains=category)
    #         results = cls.objects.all().filter(category__name__icontains=category)
    #     except:
    #         results=''

    #     return results

    # @classmethod
    # def filter_by_location(cls,location):
    #     results = cls.objects.filter(location=location)

    #     return results

    # def copy_image_url(self):
    #     return pyperclip.copy(self.image.url)


    def delete_image(self):
        return self.delete()

    # @classmethod
    # def get_image_by_id(cls,id):
    #     image = cls.objects.get(pk=id)
    #     return image
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

    def __str__(self):
        return f'{self.user.user.username} Comment on {self.image.name}'


