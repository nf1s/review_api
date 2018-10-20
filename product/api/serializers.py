from rest_framework import serializers
from reviews.models import Review, Company, Product

"""
    Serializers convert to correct datatypes JSON to Python dicts and Vice versa
    Ensure Validations for passed data
"""


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['pk', 'name', 'user', 'products']
        read_only_fields = ['pk', 'user', 'products']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['pk', 'name', 'company', 'reviews']
        read_only_fields = ['pk', 'reviews']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['pk', 'product', 'comment', 'stars', 'date']
        read_only_fields = ['pk', 'date']

    def validate_stars(self, value):
        if 0 < value <= 5:
            return value
        else:
            raise serializers.ValidationError(" Number of Stars must be a number between 0 and 5")
