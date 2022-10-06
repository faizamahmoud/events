from email.policy import default
from django.db import models
import time

# Create your models here.
class Speaker(models.Model):

    name = models.CharField(max_length=100)
    image = models.CharField(max_length=250)
    topic = models.TextField(max_length=250)
    description = models.TextField(max_length=500)
    verified_speaker = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        
        

class Event(models.Model):

    location = models.CharField(max_length=150)
    tour_date = models.CharField(max_length=150, default='TBD')
    duration = models.IntegerField(default=0)
    livestream = models.BooleanField(default=False)
    speakers = models.ForeignKey(Speaker, on_delete=models.CASCADE, related_name="events")

    def __str__(self):
        return self.location

   # Here we define the method to look at the length property and convert it
    def get_length(self):
        return time.strftime("%-M:%S", time.gmtime(self.length))
    
    
class Tour(models.Model):

    tour_name = models.CharField(max_length=150)
    tour_date = models.CharField(max_length=150, default='TBD')
    # this is going to create the many to many relationship and join table
    events = models.ManyToManyField(Event)

    def __str__(self):
        return self.tour_name
