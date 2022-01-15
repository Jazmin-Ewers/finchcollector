from django.db import models
from django.urls import reverse
from datetime import date

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

# f = Finch(species="American Goldfinch", population="43 million", habitat="Open habitats, fields, forest edges, open woodlands", threats="Cat predation, glass collisions")
# f = Finch(species="Lawrence's Goldfinch", population="240,000", habitat="Chaparral, dry areas near water", threats="Habitat loss, introduction of invasive species")
# f = Finch(species="Lesser Goldfinch", population="4.7 million", habitat="Brushy areas, forest edges, gardens", threats="Loss of riparian habitat")

class Toy(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('toys_detail', kwargs={'pk': self.id})

    
class Finch(models.Model):
  species = models.CharField(max_length=100)
  population = models.CharField(max_length=100)
  habitat = models.TextField(max_length=250)
  threats = models.TextField(max_length=250)
  toys = models.ManyToManyField(Toy)
  
  def __str__(self):
    return self.species
    
  def get_absolute_url(self):
    return reverse('finches_detail', kwargs={'finch_id': self.id})

class Feeding(models.Model):
  date = models.DateField()
  meal = models.CharField(
    max_length=1,
    choices=MEALS,
    default=MEALS[0][0]
  )
  finch = models.ForeignKey(Finch, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_meal_display()} on {self.date}"

  class Meta:
    ordering = ['-date']



