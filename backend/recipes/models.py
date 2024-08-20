# from django.db import models

# recipes/models.py
from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image_url = models.URLField()
    # image = models.ImageField(upload_to='recipes/images')
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.title
