from django.db import models
from datetime import datetime
from PIL import Image

class Realtor(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=30)
    email = models.EmailField()
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateTimeField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.photo.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.photo.path)