
from rest_framework import generics
from api.serializers import ReviewSerializer
from reviews.models import Company, Product, Review



class ReviewRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = ReviewSerializer
#    queryset = Review.objects.all()

    def get_queryset(self):
        return Review.objects.all()

