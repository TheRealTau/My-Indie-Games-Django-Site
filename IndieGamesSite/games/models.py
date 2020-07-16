from django.db import models
from publishers.models import Publisher
from functools import partial
from taggit.managers import TaggableManager


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
        verbose_name = "Game"
        verbose_name_plural = "Games"
        ordering = ['title']
    
    title = models.CharField(max_length=100, verbose_name='Title')
    about = models.TextField(verbose_name='About this game', blank=True, default='')
    publisher = models.ForeignKey(Publisher, max_length=100, verbose_name='Publisher', on_delete=models.CASCADE, blank=True)
    release_date = models.DateField(verbose_name='Official Release date')
    cover = models.ImageField(blank=True, verbose_name='Cover image', upload_to=partial(custom_game_upload, prefix='cover'))
    preview_picture = models.ImageField(blank=True, verbose_name='Preview image', upload_to=partial(custom_game_upload, prefix='preview'))
    steam_link = models.URLField(blank=True, verbose_name='Link to steam page')
    tags = TaggableManager(verbose_name='Tags')
    pub_date = models.DateField(auto_now=True, verbose_name="Published date")
