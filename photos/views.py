from django.shortcuts import render

# Create your views here.


def home(request):

    return render(request, 'index.html')


def profile(request):
    user = request.user

    return render(request,'profile/profile.html', {'user':user})