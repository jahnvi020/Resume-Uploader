from django.contrib import admin
from .models import resume

@admin.register(resume)
class ResumeModelAdmin(admin.ModelAdmin):
    list_display= ['id','name','email','dob','gender','locality','city','pin','state', 
    'mobile','jobtype','jobcity','profile_image','doc'
    ]