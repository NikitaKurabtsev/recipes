from django.db import models


class Difficult(models.Model):
    CHOICES = (
        ('EASY', 'Easy'),
        ('MEDIUM', 'Medium'),
        ('HARD', 'Hard')
    )
    difficult = models.CharField(max_length=10, choices=CHOICES, blank=False)

    def __str__(self):
        return self.difficult

class Recipe(models.Model):
    name = models.CharField(max_length=50, blank=False)
    description = models.TextField(max_length=1024, blank=False)
    difficult = models.ForeignKey(Difficult, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name
