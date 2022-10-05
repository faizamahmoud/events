from django.shortcuts import render
from django.views import View # <- View class to handle requests
from django.http import HttpResponse # <- a class to handle sending a type of response
# This will import the class we are extending 
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Speaker
from django.views.generic.base import TemplateView

# Create your views here.

# Here we will be creating a class called Home and extending it from the View class
class Home(View):

    # Here we are adding a method that will be run when we are dealing with a GET request
    def get(self, request):
        # Here we are returning a generic response
        # This is similar to response.send() in express
        return HttpResponse("Events Home")
#...
class About(View):

    def get(self, request):
        return HttpResponse("Events About")
    
class Home(TemplateView):
    template_name = "home.html"
    
#...
class About(TemplateView):
    template_name = "about.html"


 #adds artist class for mock database data
# class Speakers:
#     def __init__(self, name, image, topic,  description):
#         self.name = name
#         self.image = image
#         self.topic = topic
#         self.description = description


# speakers = [
#   Speakers("Eric", "https://i.scdn.co/image/ab67616d00001e0295cf976d9ab7320469a00a29",
#           "Topic1", "Description1"),
#   Speakers("Hazel",
#           "https://i.scdn.co/image/58518a04cdd1f20a24cf0545838f3a7b775f8080", "Welcome 👋 The Amazing Beebo was working", "Topic2"),
  
# ]

class SpeakersList(TemplateView):
    template_name = "speakers_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name") 
        if name != None:
            # .filter is the sql WHERE statement and name__icontains is doing a search for any name that contains the query param
            context["speaker"] = Speaker.objects.filter(name__icontains=name)
            context["header"] = f"Searching for {name}"
        else:
            context["speaker"] = Speaker.objects.all() # SELECT * FROM table
            context["header"] = "Trending Speakers"
        return context
        
        

class ArtistCreate(CreateView):
    model = Speaker
    fields = ['name', 'image', 'topic', 'description', 'verified_artist']
    template_name = "speakers_create.html"
    success_url = "/speakers/"
            
        