from django.contrib import admin
from .models import Teachers
class TeachersAdmin(admin.ModelAdmin):
    list_display = ("fname","lname","email","subjects", "profilepic",)

admin.site.register(Teachers,TeachersAdmin)

