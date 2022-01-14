from django.db import models
from django.urls import reverse
# Create your models here.


class Location(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}-{self.address}'


class Participant(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email


class Meetup(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.FileField(upload_to="images")
    location = models.ForeignKey(Location, null=True, on_delete=models.CASCADE)
    participants = models.ManyToManyField(Participant, blank=True)
    organiser = models.EmailField()
    date = models.DateField()

    def __str__(self):
        return f'{self.title}-{self.slug}'

    def get_absolute_url(self):
        return reverse('meetup-details', kwargs={'slug': self.slug})


