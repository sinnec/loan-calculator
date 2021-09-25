from django.db import models

# Create your models here.
class Plan(models.Model):
    class_name = models.CharField(max_length=25)
    available_plans = models.PositiveIntegerField()
    amount = models.PositiveIntegerField()
    months = models.PositiveIntegerField()

    def __str__(self):
        return self.class_name