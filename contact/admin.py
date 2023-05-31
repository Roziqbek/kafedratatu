from django.contrib import admin
from .models import *

class ContactAdmin(admin.ModelAdmin):
  list_display = ['name','email','subject','message']
  search_fields = ['name']

class TeacherAdmin(admin.ModelAdmin):
  list_display = ['name','occupation']
  search_fields = ['name']

admin.site.register(ContactModel,ContactAdmin)
admin.site.register(TeacherModell,TeacherAdmin)

admin.site.register(InfoModell)
admin.site.register(DocumentModel)