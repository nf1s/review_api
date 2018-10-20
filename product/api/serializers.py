
from rest_framework import serializers
from reviews.models import Review

"""
    Serializers convert to correct datatypes JSON to Python dicts and Vice versa
    Ensure Validations for passed data
"""


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:

        model = Review
        fields = [
            'pk',
            'comment',
            'stars',
            'date',
        ]

        read_only_fields = ['pk']

    def validate_stars(self, value):
        print("something")
        if value > 0 and value <= 5:
            return value
        else:
            raise serializers.ValidationError(" Number of Stars must be a number between 0 and 5")
