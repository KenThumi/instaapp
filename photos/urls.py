
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('profile/',views.profile, name='profile'),
    path('addprof/<int:id>',views.addprof, name='addprof'),
    path('upload/',views.upload,name='upload'),
    path('openimage/<int:image_id>',views.openimage,name='openimage')
]