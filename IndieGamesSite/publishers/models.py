from django.db import models
from functools import partial
import os


def custom_pub_upload(instance, file_name, prefix):
    if instance.pk:
        old_instance = Publisher.objects.get(pk=instance.pk)
        if prefix == 'cover':
            old_instance.cover.delete()
        elif prefix == 'profile':
            old_instance.profile_picture.delete()
    return "publisher/{0}_{1}_{2}".format(str(instance.pk), prefix, file_name)

# Create your models here.
class Publisher(models.Model):
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Editor"
        verbose_name_plural = "Editores"
        ordering = ['-name']
    
    name = models.CharField(max_length=100, verbose_name='Publisher name')
    about = models.TextField(verbose_name='About the publisher', blank=True, default='')
    cover = models.ImageField(blank=True, verbose_name="Cover image", upload_to=partial(custom_pub_upload, prefix='cover'))
    profile_picture = models.ImageField(blank=True, verbose_name="Publisher profile image", upload_to=partial(custom_pub_upload, prefix='profile'))
    site_link = models.URLField(blank=True, verbose_name='Link to official studio site')
