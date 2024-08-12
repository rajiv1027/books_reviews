import pytest
from jktech_app.serializers import BookSerializer, ReviewSerializer, GenerateSummarySerializer
from jktech_app.models import Book, Review


@pytest.mark.django_db
def test_book_serializer():
    book = Book.objects.create(
        title='Test Book',
        author='Author Name',
        summary='This is a summary.',
        genre='Fiction',
        year_published=2009,
    )
    serializer = BookSerializer(book)
    assert serializer.data['title'] == 'Test Book'


@pytest.mark.django_db
def test_generate_summary_serializer():
    data = {'content': 'Some content'}
    serializer = GenerateSummarySerializer(data=data)
    assert serializer.is_valid()
    assert 'content' in serializer.validated_data


@pytest.mark.django_db
def test_review_serializer():
    book = Book.objects.create(
        title='Test Book',
        author='Author Name',
        summary='This is a summary.',
        genre='Fiction',
        year_published=2009,
    )
    review = Review.objects.create(
        book=book,
        user_id='1',
        review_text='This is a review.',
        rating=4,
    )
    serializer = ReviewSerializer(review)
    assert serializer.data['book'] == book.id
    assert serializer.data['user_id'] == '1'
    assert serializer.data['review_text'] == 'This is a review.'
    assert serializer.data['rating'] == 4
