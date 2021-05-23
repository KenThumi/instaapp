from django import forms
from .models import Image, Profile, Comment

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ImageForm(forms.ModelForm):
  class Meta:
      model = Image
      exclude = ['likes','profile','comments']
    #   fields = '__all__'


class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    exclude = ['user','image']