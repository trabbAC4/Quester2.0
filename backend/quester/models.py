from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class Quester(models.Model):
    title = models.CharField(max_length = 120)
    description = models.CharField(max_length = 120)
    level = models.IntegerField(validators=[MaxValueValidator(limit_value=100)]) 
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title




