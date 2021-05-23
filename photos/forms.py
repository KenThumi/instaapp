from django import forms
from .models import Image, Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ImageForm(forms.ModelForm):
  class Meta:
      model = Image
      exclude = ['likes','profile','comments']
    #   fields = '__all__'