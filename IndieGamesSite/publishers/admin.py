from django.contrib import admin
from .models import Publisher

# Register your models here.
class PublisherAdmin(admin.ModelAdmin):
    # Missing about
    list_display = ('name','cover','profile_picture','site_link')

admin.site.register(Publisher, PublisherAdmin)
