from django.db import models
from publishers.models import Publisher

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