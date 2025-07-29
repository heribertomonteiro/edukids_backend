from django.db import models

# Create your models here.

class Post(models.Model):
    titulo = models.CharField(max_length=30)
    descricao = models.CharField(max_length=750)
    data = models.DateField(auto_now_add=True)
    imagem = models.ImageField(upload_to='imagens/', blank=True, null=True, default='')