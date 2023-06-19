from django.db import models
from django.urls import reverse
from datetime import date

# Create your models here.

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

class Toy(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('toys_detail', kwargs={'pk': self.id})

class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100,)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    #creating M2M relationship
    toys = models.ManyToManyField(Toy)


    #Changin instance method
    def __str__(self):
        return f'{self.name} ({self.id})'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pokemon_id': self.id})

    def fed_for_today(self):
        return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)

class Feeding(models.Model):
    date = models.DateField('feeding-date')
    meal = models.CharField(
        max_length=1,
        choices=MEALS,
        default=MEALS[0][0]
    )

    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_meal_diplay()} on {self.date}"

    #change the default sort
    class Meta:
        ordering = ['-date']
