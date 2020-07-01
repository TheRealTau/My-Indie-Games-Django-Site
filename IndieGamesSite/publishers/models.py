from django.db import models


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
