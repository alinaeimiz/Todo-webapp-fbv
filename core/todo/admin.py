from django.contrib import admin
from .models import ToDo
# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    list_display=['author','task','completed','created_date']
    fields = ['author', 'task','completed']
    list_filter =('created_date', 'updated_date')
    
admin.site.register(ToDo,TodoAdmin)    