from django.db import models


class Musico(models.Model):
	nome = models.CharField(max_length=100)
	genero = models.CharField(max_length=100)


	def __str__(self):
		return self.nome

class Banda(models.Model):
	nome = models.CharField(max_length=100)
	musicos = models.ManyToManyField(Musico, related_name='bandas')
	estilo_musical = models.ForeignKey(EstiloMusical, on_delete=models.PROTECT)

	def __str__(self):
		return self.nome

class EstiloMusical(models.Model):
	estilo = models.CharField(max_length=100)

	def __str__(self):
		return self.estilo