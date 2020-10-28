from django.db import models

# Create your models here.

class ImageFile(models.Model):
    # https://docs.djangoproject.com/en/3.1/ref/models/fields/#filefield
    image = models.FileField()
    image_data = models.BinaryField(null=True)