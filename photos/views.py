from django.contrib.auth.models import User
from photos.forms import CommentForm, ImageForm, ProfileForm
from django.shortcuts import render,redirect
import cloudinary.uploader
from .models import Image, Profile
from django.contrib import messages
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
            upload_result = cloudinary.uploader.upload(file_to_upload)
            new_result = remove_prefix(upload_result['secure_url'],'https://res.cloudinary.com/dtw9t2dom/')

            image = Image(image=new_result,
                          name=form.cleaned_data['name'],
                          caption=form.cleaned_data['caption'],
                          profile=request.user.profile,)

            image.save_image()

            messages.success(request, 'Successful upload.')
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



def comment(request,image_id):
    image = Image.objects.get(pk=image_id)

    if request.method=='POST':
            form = CommentForm(request.POST,request.FILES)
        
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user.profile
                comment.image = image
                comment.save()

                return redirect('openimage', image_id)


    return render(request,'commentForm.html', {'form': CommentForm()})


def edit(request,image_id):
    image = Image.objects.get(pk=int(image_id))

    if request.method=='POST':
        form = ImageForm(request.POST,request.FILES)
    
        try:
            file_to_upload = request.FILES['image']
        except:
            messages.error(request, 'Kindly select an image.')
           
      
        if form.is_valid():
           
            if file_to_upload:
                upload_result = cloudinary.uploader.upload(file_to_upload)
                new_result = remove_prefix(upload_result['secure_url'],'https://res.cloudinary.com/dtw9t2dom/')

                image_result = new_result if new_result else image.image

                update_details = {'image':image_result,
                                'name':form.cleaned_data['name'],
                                    'caption':form.cleaned_data['caption'],
                                    'profile':request.user.profile}

                Image.update_caption(update_details,image_id)

                messages.success(request, 'Successful edit.')
                return redirect('openimage', image_id)



    form = ImageForm(instance=image)

    ctx = {'form':form}

    return render(request,'upload.html',ctx)


def delete_image(request,image_id):
    image = Image.objects.get(pk=int(image_id))

    for comment in image.comments.all():  #delete any comments
           comment.delete()

    image.delete_image()

    messages.success(request, 'Image Deleted successfully.')
    
    return redirect('home')



def search(request):

    if request.method=='POST':

        needle = request.POST['search']

        images=Image.objects.filter(name__icontains=needle).all()

        users = user = User.objects.exclude(username=request.user.username) 

        ctx = {'images':images, 'users':users, 'search_results':f'Search Results ({images.count()})'}

        return render(request, 'index.html',ctx)

    return redirect('home')
