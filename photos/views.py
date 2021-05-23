from photos.forms import ImageForm, ProfileForm
from django.shortcuts import render,redirect
import cloudinary.uploader
from .models import Profile

# Create your views here.


def home(request):

    return render(request, 'index.html')


def profile(request):
    user = request.user

    return render(request,'profile/profile.html', {'user':user})


def addprof(request,id):
    form = ProfileForm()

    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES)

        file_to_upload = request.FILES['profile_photo']

        if form.is_valid():
            upload_result = cloudinary.uploader.upload(file_to_upload)
            new_result = remove_prefix(upload_result['secure_url'],'https://res.cloudinary.com/dtw9t2dom/')

            profile = Profile(profile_photo=new_result,
                              bio=form.cleaned_data['bio'],
                              user=request.user)

            profile.save_profile()

            # messages.success(request, 'Successful upload.')
            return redirect('profile')

    ctx = {'form':form}

    return render(request,'profile/update.html',ctx)



def remove_prefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix):]
    return text


def upload(request):
    form = ImageForm()

    # if request.method=='POST':
    #     form = ImageForm(request.POST,request.FILES)

    #     file_to_upload = request.FILES['image']
      
    #     if form.is_valid():
    #         upload_result = cloudinary.uploader.upload(file_to_upload)
    #         new_result = remove_prefix(upload_result['secure_url'],'https://res.cloudinary.com/dtw9t2dom/')

    #         image = Image(image=new_result,
    #                       name=form.cleaned_data['name'],
    #                       description=form.cleaned_data['description'],
    #                       category=form.cleaned_data['category'],
    #                       location = form.cleaned_data['location'])

    #         image.save_image()

    #         messages.success(request, 'Successful upload.')
    #         return redirect('home')

    ctx = {'form':form}
    return render(request,'upload.html',ctx)