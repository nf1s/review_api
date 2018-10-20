
from rest_framework import generics
from api.serializers import ReviewSerializer, CompanySerializer, ProductSerializer
from reviews.models import Company, Product, Review


class CompanyRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = CompanySerializer

    def get_queryset(self):
        return Company.objects.all()

class ProductRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all()


class ReviewRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.all()

