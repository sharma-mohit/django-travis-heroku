from django.contrib import admin

# Register your models here.
from models import todo #Import our todo Model.
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.contrib.auth.models import Group

admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.unregister(Site)

admin.site.register(todo) #Register the model with the admin
