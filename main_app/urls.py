from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"), 
    path('about/', views.About.as_view(), name="about"), 
    path('speakers/', views.SpeakersList.as_view(), name="speakers_list"), 
    path('speakers/new/', views.SpeakersCreate.as_view(), name="speakers_create"), 
    path('speakers/<int:pk>/', views.SpeakersDetail.as_view(), name="speakers_detail"),
    path('speakers/<int:pk>/update',views.SpeakersUpdate.as_view(), name="speakers_update"),
    path('speakers/<int:pk>/delete',views.SpeakersDelete.as_view(), name="speakers_delete"),
    path('speakers/<int:pk>/events/new/', views.EventCreate.as_view(), name="event_create")
]
