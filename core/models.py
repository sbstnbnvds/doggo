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
        global ext
        if self.breed == 'DM':
            ext = 'doberman.jpg'
        elif self.breed == 'CR':
            ext = 'corgi.jpg'
        elif self.breed == 'MX':
            ext = 'mix.jpeg'
        elif self.breed == 'BG':
            ext = 'beagle.jpg'
        elif self.breed == 'RW':
            ext = 'rottweiler.jpg'
        img_url = 'breeds/' + ext

        return img_url

    def long_breed(self):
        x = self.img_url()
        x1 = x.split('.')
        x2 = x1[0]
        x3 = x2.split('/')
        long_breed = x3[1]

        return long_breed
        