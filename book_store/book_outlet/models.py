from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=3)

    def __str__(self):
        return f"{self.name} {self.code}"

    class Meta:
        verbose_name_plural = "Countries"


class Address(models.Model):
    street = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=6)
    city = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.street} {self.city} {self.postal_code}"

    class Meta:
        verbose_name_plural = "Address Entries"

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(Address,on_delete=models.SET_NULL,null=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=100)
    rating = models.IntegerField(
        validators=[MinValueValidator(1),MaxValueValidator(10)]
    )
    author = models.ForeignKey(Author,on_delete=models.CASCADE,related_name="books")
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(db_index=True)
    published_countries = models.ManyToManyField(Country, related_name="books")

    '''
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    '''

    def __str__(self):
        return f'{self.title}({self.rating})'

    def get_absolute_url(self):
        return reverse("book-details-slug-page", args=[self.slug])


