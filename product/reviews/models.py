from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from django.db import models
from django.conf import settings
from django.urls import reverse
from rest_framework.reverse import reverse as api_reverse

# ----------------------------------------- VALIDATORS ------------------------------------------------#
alphanumeric = RegexValidator(r'^[0-9a-zA-Z\s]*$', 'Only alphanumeric characters are allowed.')
numeric = RegexValidator(r'^[0-9]*$', 'Only numeric digits are allowed.')
min_stars = MinValueValidator(1, 'Number of stars cannot be less than 1')
max_stars = MaxValueValidator(5, 'Number of stars cannot exceed 5')

# -------------------------------------------- MODELS -------------------------------------------------#


# --------------------------------------- COMPANY MODEL -----------------------------------------------#

class Company(models.Model):
    class Meta:
        verbose_name_plural = "Companies"

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=128, validators=[alphanumeric])

    def __str__(self):
        return self.name

    def get_api_url(self, request=None):
        return api_reverse('api_v1:company-rud', kwargs={'pk': self.pk}, request=request)

# --------------------------------------- PRODUCT MODEL -----------------------------------------------#


class Product(models.Model):

    class Meta:
        verbose_name_plural = "Products"

    company = models.ForeignKey('reviews.Company', on_delete=models.PROTECT, related_name='products')
    name = models.CharField('Product Name', max_length=128, validators=[alphanumeric])

    def __str__(self):
        return self.name

    def get_api_url(self, request=None):
        return api_reverse('api_v1:product-rud', kwargs={'pk': self.pk}, request=request)

# --------------------------------------- REVIEW MODEL ------------------------------------------------#


class Review(models.Model):
    class Meta:
        verbose_name_plural = "Reviews"

    product = models.ForeignKey('reviews.Product', on_delete=models.PROTECT,
                                related_name='reviews', validators=[alphanumeric])
    comment = models.CharField('Review comment', max_length=128, validators=[alphanumeric])
    stars = models.IntegerField('Number of stars', validators=[numeric, min_stars, max_stars])
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.stars) + " Stars"

    def get_api_url(self, request=None):
        return api_reverse('api_v1:review-rud', kwargs={'pk': self.pk}, request=request)
