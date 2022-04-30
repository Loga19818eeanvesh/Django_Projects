from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator

# Create your models here.

class Review(models.Model):
    user_name = models.CharField(max_length=50,validators=[MinLengthValidator(5)])
    review_text = models.TextField(max_length=200)
    rating = models.IntegerField(
        validators=[MinValueValidator(1),MaxValueValidator(10)]
    )

