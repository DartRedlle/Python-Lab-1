from django.contrib import admin
from .models import Massage

# Register your models here.
#admin.site.register(Massage)

class MassageAdmin(admin.ModelAdmin):
   list_display = ('author','header','text')

# Register the admin class with the associated model
admin.site.register(Massage, MassageAdmin)
