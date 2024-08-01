from rest_framework import serializers
from jktech_app.models import Book, Review


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    rating = serializers.FloatField()

    class Meta:
        model = Review
        fields = '__all__'

    def validate_rating(self, value):
        if not (0.0 <= value <= 10.0):
            raise serializers.ValidationError("Rating must be between 0.0 and 10.0")
        return value

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # Ensure that rating is returned as a number
        if isinstance(representation['rating'], str):
            representation['rating'] = float(representation['rating'])
        return representation


class GenerateSummarySerializer(serializers.Serializer):
    content = serializers.CharField()
