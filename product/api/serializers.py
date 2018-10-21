from rest_framework import serializers
from reviews.models import Review, Company, Product

"""
    Serializers convert to correct datatypes JSON to Python dicts and Vice versa
    Ensure Validations for passed data
"""


class CompanySerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Company
        fields = ['url', 'name']
        read_only_fields = ['url']

    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)


class ProductSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)
    company = CompanySerializer(read_only=True)
    class Meta:
        model = Product
        fields = ['url', 'pk', 'name', 'company']
        read_only_fields = ['pk', 'company']

    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)



class ReviewSerializer(serializers.ModelSerializer):

    url = serializers.SerializerMethodField(read_only=True)
    product = ProductSerializer(read_only=True)
    class Meta:
        model = Review
        fields = ['url', 'pk', 'product', 'comment', 'stars', 'date']
        read_only_fields = ['pk', 'date', 'product']

    def validate_stars(self, value):
        if 0 < value <= 5:
            return value
        else:
            raise serializers.ValidationError(" Number of Stars must be a number between 0 and 5")

    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)

