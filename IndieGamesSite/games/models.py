from django.db import models
from publishers.models import Publisher
from functools import partial


def custom_game_upload(instance, file_name, prefix):
    if instance.pk:
        old_instance = Game.objects.get(pk=instance.pk)
        if prefix == 'cover':
            old_instance.cover.delete()
        elif prefix == 'preview':
            old_instance.preview_picture.delete()
    return "game/{0}_{1}_{2}".format(str(instance.pk), prefix, file_name)

# Create your models here.
class Game(models.Model):
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Juego"
        verbose_name_plural = "Juegos"
        ordering = ['-title']
    
    title = models.CharField(max_length=100, verbose_name='Titulo')
    publisher = models.ForeignKey(Publisher, max_length=100, verbose_name='Editor', on_delete=models.CASCADE, blank=True)
    release_date = models.DateField(verbose_name='Fecha de publicación')
    image = models.ImageField(blank=True, verbose_name='Imagen', upload_to=custom_game_upload)
    steam_link = models.URLField(blank=True, verbose_name='Link a pagina de steam')
