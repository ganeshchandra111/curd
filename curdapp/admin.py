from django.contrib import admin
from .models import Student

# Register your models here.

model_list = [Student]

admin.site.register(model_list)