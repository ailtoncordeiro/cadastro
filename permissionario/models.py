from django.db import models

# Create your models here.

class Permissionario(models.Model):
    nome = models.CharField(max_length=30, verbose_name='Nome')
    sobrenome = models.CharField(max_length=150, verbose_name='Sobrenome')
    cpf = models.CharField(max_length=14, verbose_name='CPF')

    #Metódo que será lido pelo admin para exibição da instância
    def __str__(self):
        return "{}".format(self.nome)
