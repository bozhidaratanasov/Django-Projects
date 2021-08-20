from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=30, blank=False)
    image_url = models.URLField(blank=False)
    description = models.TextField(blank=False)
    ingredients = models.CharField(max_length=250, blank=False)
    time = models.IntegerField(blank=False)
    
    def __str__(self) -> str:
        return f"{self.title}"
