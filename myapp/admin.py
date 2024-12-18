from django.contrib import admin
from .models import Project,Contact
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display=['id','title','desc','img','srclink','cat','tech']

class ContactAdmin(admin.ModelAdmin):
    list_display=['id','fname','lname','email','mob','msg']
    
admin.site.register(Project,ProjectAdmin)
admin.site.register(Contact,ContactAdmin)