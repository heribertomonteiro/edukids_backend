# seeds.py
import os
import django
from random import choice

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "edukids.settings")
django.setup()

from home.models import Post  # ajuste se seu app tiver outro nome

titulos = [
    "Primeiro Post",
    "Novidade Incrível",
    "Django na prática",
    "Como usar o Admin",
    "Melhores dicas de Python",
]

descricoes = [
    "Este é um post de teste com uma descrição mais longa.",
    "Outro exemplo de post para popular o banco.",
    "Django é um framework poderoso e produtivo.",
    "Você pode usar o shell, admin ou scripts para popular.",
    "Este conteúdo é apenas um exemplo para desenvolvimento.",
]

# Cria 10 posts aleatórios
for i in range(10):
    Post.objects.create(
        titulo=choice(titulos),
        descricao=choice(descricoes)
    )

print("✅ Banco de dados populado com 10 posts de exemplo!")
