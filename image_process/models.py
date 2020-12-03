from django.db import models

# Create your models here.

class ImageFile(models.Model):
    # https://docs.djangoproject.com/en/3.1/ref/models/fields/#filefield
    image = models.FileField()
    image_data = models.BinaryField(null=True)

# This model maps to the applyblur view which
# calls the plpython function
# We use a view because
class BlurredImage(models.Model):
    img_id = models.AutoField(primary_key=True)
    img_binary = models.BinaryField()

    class Meta:
        managed = False
        db_table = 'applyblur'