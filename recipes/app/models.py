from django.db import models


class Recipe(models.Model):
    CHOICES = (
        ('EASY', 'Easy'),
        ('MEDIUM', 'Medium'),
        ('HARD', 'Hard')
    )
    name = models.CharField(max_length=50, blank=False)
    description = models.TextField(max_length=1024, blank=False)
    difficult = models.CharField(max_length=10, choices=CHOICES, blank=False)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name
