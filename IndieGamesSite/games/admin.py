from django.contrib import admin
from .models import Game

# Register your models here.
class GameAdmin(admin.ModelAdmin):
    # Missing about
    list_display = ('title','publisher','release_date','cover','preview_picture','steam_link','tags')
    readonly_fields = ('pub_date',)

admin.site.register(Game, GameAdmin)

