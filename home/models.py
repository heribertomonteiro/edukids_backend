from django.db import models
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    titulo = models.CharField(max_length=30)
    descricao = models.CharField(max_length=750)
    data = models.DateField(auto_now_add=True)
    imagem = models.ImageField(upload_to='imagens/', blank=True, null=True, default='')

class Evento(models.Model):
    titulo = models.CharField(max_length=200)
    data = models.DateField()
    descricao = models.TextField(blank=True)

    def __str__(self):
        return f"{self.titulo} ({self.data})"
    
    def get_absolute_url(self):
        return reverse('evento', args=[str(self.id)])