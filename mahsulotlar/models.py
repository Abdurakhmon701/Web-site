from django.db import models

class Mahsulotlar(models.Model):
	sarlavhasi = models.CharField(max_length=200) 
	tasnifi = models.TextField()

	def __str__(self):
		return self.sarlavhasi

# ==> python manage.py makemigrations
# ==> python manage.py migrate
# superuser yaratish uchun
# ==> python manage.py 