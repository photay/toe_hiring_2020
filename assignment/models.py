from django.db import models

class DemoModel(models.Model):
    demo_field = models.CharField(verbose_name="Demo Field",max_length=100, blank=False)

# TODO: Put your dog questions model here
