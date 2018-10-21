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

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class CompanyRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = CompanySerializer

    def get_queryset(self):
        user = self.request.user
        return Company.objects.filter(user=user)

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


# -------------------------- Product Views ------------------------------------ #


class ProductAPIView(generics.ListCreateAPIView):
    lookup_field = 'pk'
    serializer_class = ProductSerializer

    def get_queryset(self):
        user = self.request.user
        company = Company.objects.get(user=user)
        return Product.objects.filter(company=company)

    def perform_create(self, serializer):
        user = self.request.user
        company = Company.objects.get(user=user)
        serializer.save(company=company)

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class ProductRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = ProductSerializer

    def get_queryset(self):
        user = self.request.user
        company = Company.objects.get(user=user)
        return Product.objects.filter(company=company)

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


# -------------------------- Review Views ------------------------------------ #


class ReviewAPIView(generics.ListCreateAPIView):
    lookup_field = 'pk'
    serializer_class = ReviewSerializer

    def get_queryset(self):
        product_id = self.request.path.split("/")[-3]
        return Review.objects.filter(product=product_id)

    def perform_create(self, serializer):
        product_id = self.request.path.split("/")[-3]
        product = Product.objects.get(pk=product_id)
        serializer.save(product=product)

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class ReviewRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}

