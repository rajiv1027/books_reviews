from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator

current_year = timezone.now().year


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    year_published = models.IntegerField(
        validators=[
            MinValueValidator(1500),
            MaxValueValidator(current_year)
        ]
    )
    summary = models.TextField()

    def __str__(self):
        return self.title


class Review(models.Model):
    id = models.AutoField(primary_key=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    user_id = models.CharField(max_length=10)
    review_text = models.TextField()
    rating = models.DecimalField(
        max_digits=4,
        decimal_places=1,
        validators=[MinValueValidator(0.0), MaxValueValidator(10.0)]
    )

    def __str__(self):
        return f'Review by {self.user_id} for {self.book.title}'
