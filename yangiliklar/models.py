from django.db import models

class YangiliklarModel(models.Model):
	sarlavhasi = models.CharField(max_length=200) 
	rasmi = models.ImageField(upload_to = 'images/')
	matni = models.TextField()
	vaqti = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.sarlavhasi