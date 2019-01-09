from django.db import models


# Create your models here.
class BlockedEmail(models.Model):
	email = models.EmailField(unique=True)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.email


class BlockedIp(models.Model):
	ip_address = models.GenericIPAddressField(unique=True)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.ip_address

class BlockedWord(models.Model):
	word = models.CharField(max_length=200, unique=True)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.word