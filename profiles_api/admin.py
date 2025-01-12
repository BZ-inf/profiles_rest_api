from django.contrib import admin
from profiles_api import models

admin.site.register(models.UserProfile) # as created custom one with email not username

# Register your models here.
