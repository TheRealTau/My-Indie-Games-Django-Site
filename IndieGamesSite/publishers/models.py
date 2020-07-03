from django.db import models


def custom_pub_upload(instance, file_name):
    if instance.pk:
        old_instance = Publisher.objects.get(pk=instance.pk)
        old_instance.image.delete()
    return 'publisher/' + file_name

# Create your models here.
class Publisher(models.Model):
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Editor"
        verbose_name_plural = "Editores"
        ordering = ['-name']
    
    name = models.CharField(max_length=100, verbose_name='Nombre')
    texto = models.TextField(verbose_name='Texto del editor', blank=True, default='')
    image = models.ImageField(blank=True, verbose_name="Imagen", upload_to=custom_pub_upload)
