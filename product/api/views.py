from rest_framework import generics
from api.serializers import ReviewSerializer, CompanySerializer, ProductSerializer
from reviews.models import Company, Product, Review
from api.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAdminUser

# -------------------------- Company Views ------------------------------------ #


class CompanyAPIView(generics.ListCreateAPIView):
    lookup_field = 'pk'
    serializer_class = CompanySerializer

    def get_queryset(self):
        user = self.request.user
        return Company.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CompanyRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = CompanySerializer

    def get_queryset(self):
        user = self.request.user
        return Company.objects.filter(user=user)

# -------------------------- Product Views ------------------------------------ #


class ProductAPIView(generics.ListCreateAPIView):
    lookup_field = 'pk'
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all()


class ProductRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all()

# -------------------------- Review Views ------------------------------------ #


class ReviewAPIView(generics.ListCreateAPIView):
    lookup_field = 'pk'
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.all()


class ReviewRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.all()
