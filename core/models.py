from django.db import models

# Create your models here.

class Dog(models.Model):
    name = models.CharField(max_length=15)
    weight = models.SmallIntegerField()
    
    breeds = [
        ('DM', 'Doberman'),
        ('CR', 'Corgi'),
        ('BG', 'Beagle'),
        ('RW', 'Rottweiler'),
        ('MX', 'Mixed'),
    ]
    
    breed = models.CharField(
        max_length = 2,
        choices = breeds,
        default = 'MX',
    )

    def img_url(self):
        if self.breed == 'DM':
            ext = 'doberman.jpg'
        elif self.breed == 'CR':
            ext = 'corgi.jpg'
        elif self.breed == 'MX':
            ext = 'mix.jpeg'
        img_url = 'breeds/' + ext 
        return img_url


