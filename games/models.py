from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=50)
    description = models.TextField()
    release_date = models.CharField(max_length=50)
    developer = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    price = models.CharField(max_length=10)

    def __str__(self):
        return self.title

