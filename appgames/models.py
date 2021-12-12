from django.db import models

# Create your models here.

class Game(models.Model):
	STATUS_CHOICES = (
		('резерв', 'Резерв'),
		('оплачена', 'Оплачена'),
		('проведена', 'Проведена'),
		('отменена', 'Отменена'),
	)
	date = models.DateTimeField()
	name = models.CharField(max_length=100)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	status = models.CharField(max_length=20, choices=STATUS_CHOICES)

	def __str__(self):
		return self.name