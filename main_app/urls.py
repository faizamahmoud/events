from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"), 
    path('about/', views.About.as_view(), name="about"), 
    path('speakers/', views.SpeakersList.as_view(), name="speakers_list"), 
    path('speakers/new/', views.SpeakersCreate.as_view(), name="speakers_create")

]
