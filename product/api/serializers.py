from rest_framework import serializers
from reviews.models import Review, Company, Product

"""
    Serializers convert to correct datatypes JSON to Python dicts and Vice versa
    Ensure Validations for passed data
"""


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['pk', 'name']
        read_only_fields = ['pk']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['pk', 'name', 'company']
        read_only_fields = ['pk', 'company']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['pk', 'product', 'comment', 'stars', 'date']
        read_only_fields = ['pk', 'date', 'product']

    def validate_stars(self, value):
        if 0 < value <= 5:
            return value
        else:
            raise serializers.ValidationError(" Number of Stars must be a number between 0 and 5")
