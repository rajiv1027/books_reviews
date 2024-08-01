from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from django.db.models import Avg
from django.shortcuts import get_object_or_404

from jktech_app.models import Book, Review
from jktech_app.serializers import BookSerializer, ReviewSerializer, GenerateSummarySerializer


class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'id'


class ReviewListCreateView(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        book_id = self.kwargs['id']
        return Review.objects.filter(book_id=book_id)

    def perform_create(self, serializer):
        book_id = self.kwargs['id']
        book = get_object_or_404(Book, id=book_id)
        serializer.save(book=book)


class BookSummaryView(APIView):
    def get(self, request, id):
        book = get_object_or_404(Book, id=id)
        reviews = Review.objects.filter(book=book)
        avg_rating = reviews.aggregate(Avg('rating'))['rating__avg'] if reviews else None
        return Response({
            'summary': book.summary,
            'average_rating': avg_rating
        })


class RecommendationsView(APIView):
    def get(self, request):
        user_id = request.user.id
        recommendations = self.get_recommendations(user_id)
        return Response(recommendations)

    def get_recommendations(self, user_id):
        reviewed_books = Review.objects.filter(user_id=user_id, rating__gte=5.0).values_list('book_id', flat=True)
        reviewed_genres = Book.objects.filter(id__in=reviewed_books).values_list('genre', flat=True).distinct()
        recommended_books = Book.objects.filter(genre__in=reviewed_genres).distinct()

        serializer = BookSerializer(recommended_books, many=True)
        return serializer.data


class GenerateSummaryView(APIView):

    @swagger_auto_schema(
        request_body=GenerateSummarySerializer,
        responses={200: openapi.Response('Summary generated', GenerateSummarySerializer)}
    )
    def post(self, request):
        serializer = GenerateSummarySerializer(data=request.data)
        if serializer.is_valid():
            content = serializer.validated_data['content']
            summary = "Can call the ChatGPT API to generate meaningful content"
            return Response({'summary': summary}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


