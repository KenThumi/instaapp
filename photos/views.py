from django.contrib.auth.models import User
from photos.forms import ImageForm, ProfileForm
from django.shortcuts import render,redirect
import cloudinary.uploader
from .models import Image, Profile
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    images = Image.objects.all()

    users = user = User.objects.exclude(username=request.user.username) 

    ctx = {'images':images, 'users':users}

    return render(request, 'index.html',ctx)


@login_required(login_url='/accounts/login/')
def profile(request):
    user = request.user

    return render(request,'profile/profile.html', {'user':user})


@login_required(login_url='/accounts/login/')
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

@login_required(login_url='/accounts/login/')
def upload(request):
    form = ImageForm()

    if request.method=='POST':
        form = ImageForm(request.POST,request.FILES)

        file_to_upload = request.FILES['image']
      
        if form.is_valid():
            print('Tuko fiti kabisa')
            upload_result = cloudinary.uploader.upload(file_to_upload)
            new_result = remove_prefix(upload_result['secure_url'],'https://res.cloudinary.com/dtw9t2dom/')

            image = Image(image=new_result,
                          name=form.cleaned_data['name'],
                          caption=form.cleaned_data['caption'],
                          profile=request.user.profile,)

            image.save_image()

            # messages.success(request, 'Successful upload.')
            return redirect('home')

    ctx = {'form':form}
    return render(request,'upload.html',ctx)


def openimage(request,image_id):
    image = Image.objects.get(pk=image_id)

    return render(request,'image.html', {'image':image})


def like(request,image_id):
    image = Image.objects.get(pk=image_id)

    image.likes = 1 if image.likes ==None else (image.likes +1)   

    image.save()

    return render(request,'image.html', {'image':image})