from django.contrib import admin
from .models import Speaker # import the Artist model from models.py
# Register your models here.

admin.site.register(Speaker) # this line will add the model to the admin panel