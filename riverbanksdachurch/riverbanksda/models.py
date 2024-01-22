# riverbanksda/models.py

from django.db import models

class SpiritualBook(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    document = models.FileField(upload_to='books/')  # Ensure 'upload_to' is set to the correct path
    cover_image = models.ImageField(upload_to='books/', blank=True)
    uploaded_by = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
