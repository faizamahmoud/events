from django.contrib import admin
from .models import Speaker, Event, Tour # import the Artist model from models.py
# Register your models here.

admin.site.register(Speaker) # this line will add the model to the admin panel
admin.site.register(Event)
admin.site.register(Tour)