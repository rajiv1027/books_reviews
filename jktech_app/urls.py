from django.urls import path, include

from jktech_app.views import (
    BookListCreateView,
    BookDetailView,
    ReviewListCreateView,
    BookSummaryView,
    RecommendationsView,
    GenerateSummaryView
)

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:id>/', BookDetailView.as_view(), name='book-detail'),
    path('books/<int:id>/reviews/', ReviewListCreateView.as_view(), name='book-reviews'),
    path('books/<int:id>/summary/', BookSummaryView.as_view(), name='book-summary'),
    path('recommendations/', RecommendationsView.as_view(), name='recommendations'),
    path('generate-summary/', GenerateSummaryView.as_view(), name='generate-summary')
]