from django.db import models
from multiselectfield import MultiSelectField

class DemoModel(models.Model):
    demo_field = models.CharField(verbose_name="Demo Field",max_length=100, blank=False)

# TODO: Put your dog questions model here
TRICKS = (('item_key1', 'Sit'),
              ('item_key2', 'Fetch'),
              ('item_key3', 'Stay'),
              ('item_key4', 'Roll Over'))

class DogQuestion(models.Model):
	daily_walk = models.BooleanField()
	dog_breed = models.CharField(max_length=100, blank=False)
	dog_age = models.IntegerField()
	dog_tricks = MultiSelectField(choices=TRICKS)
	email = models.CharField(max_length=100, blank=False)