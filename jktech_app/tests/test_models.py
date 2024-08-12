import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from jktech_app.models import Book, Review


@pytest.mark.django_db
def test_book_creation():
    client = APIClient()
    response = client.post(reverse('book-list-create'), {
        'title': 'Test Book',
        'year_published': 2009,
        'author': 'Author Name',
        'summary': 'This is a summary.',
        'genre': 'Fiction',
    })
    assert response.status_code == status.HTTP_201_CREATED
    assert Book.objects.count() == 1
    assert Book.objects.get().title == 'Test Book'


@pytest.mark.django_db
def test_review_creation():
    book = Book.objects.create(
        title='Test Book',
        year_published=2009,
        author='Author Name',
        summary='This is a summary.',
        genre='Fiction',
    )
    client = APIClient()
    data = {
        'user_id': '123',
        'rating': 5.0,
        'review_text': 'Excellent book!',
        'book': book.id
    }
    response = client.post(reverse('book-reviews', kwargs={'id': book.id}), data)
    assert response.status_code == status.HTTP_201_CREATED
    assert Review.objects.count() == 1
    review = Review.objects.get()
    assert review.rating == 5.0
    assert review.review_text == 'Excellent book!'
    assert review.book == book
    assert review.user_id == '123'