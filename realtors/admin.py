from django.contrib import admin
from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'hire_date', 'email')
    list_display_links = ('id', 'name')
    list_filter = ('name','email')
    search_fields = ('id','name','email')
   
    
admin.site.register(Realtor, RealtorAdmin)

