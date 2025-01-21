from django.db import models
from musician.models import Musician  


class Album(models.Model):
    ratings = [
        (1, '1 star'),
        (2, '2 star'),
        (3, '3 star'),
        (4, '4 star'),
        (5, '5 star'),
    ]

    name = models.CharField(max_length=255)  
    musician = models.ForeignKey(
        Musician, 
        on_delete=models.CASCADE, 
        related_name='albums'
    )  
    release_date = models.DateField()
    rating = models.PositiveSmallIntegerField(
        choices=ratings,
    )

    def __str__(self):
        return f"{self.name} by {self.musician.first_name} {self.musician.last_name}"
