import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from jktech_app.models import Book, Review


@pytest.mark.django_db
def test_book_list_view():
    client = APIClient()
    Book.objects.create(
        title='Test Book',
        year_published=2009,
        author='Author Name',
        summary='This is a summary.',
        genre='Fiction'
    )
    response = client.get(reverse('book-list-create'))
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1


@pytest.mark.django_db
def test_book_summary_view():
    book = Book.objects.create(
        title='Test Book',
        year_published=2009,
        author='Author Name',
        summary='This is a summary.',
        genre='Fiction'
    )
    Review.objects.create(
        book=book,
        user_id=1,
        rating=4.0,
        review_text='Good book'
    )
    client = APIClient()
    response = client.get(reverse('book-summary', kwargs={'id': book.id}))
    assert response.status_code == status.HTTP_200_OK
    assert 'summary' in response.data
    assert 'average_rating' in response.data


@pytest.mark.django_db
def test_generate_summary_view():
    client = APIClient()
    url = reverse('generate-summary')
    data = {
        'content': 'This is some content that needs summarizing.'
    }
    response = client.post(url, data, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert 'summary' in response.data
    assert response.data['summary'] == "Can call the ChatGPT API to generate meaningful content"

    invalid_data = {}
    invalid_response = client.post(url, invalid_data, format='json')
    assert invalid_response.status_code == status.HTTP_400_BAD_REQUEST
    assert 'content' in invalid_response.data