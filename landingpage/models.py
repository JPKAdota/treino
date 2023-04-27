from django.db import models

# models.py
class Image(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='images/')


    class Meta:
        app_label = 'landingpage' # nome do seu aplicativo
