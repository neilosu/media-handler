from django.db import models

class ImageUpload(models.Model):
    image = models.BinaryField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
    image_name = models.CharField(max_length=255, default='image_name')
