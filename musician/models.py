from django.db import models

class Musician(models.Model):
    ins_choices = [
        ('guitar', 'Guitar'),
        ('piano', 'Piano'),
        ('other', 'Other'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)  
    instrument_type = models.CharField(max_length=50, choices=ins_choices)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
