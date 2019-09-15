from django.contrib.auth.models import User
from django.db import models

class Avaliacao(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	comentario = models.TextField(null=True, blank=True)
	note = models.DecimalField(max_digits=3, decimal_places=2)
	data = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.user.username