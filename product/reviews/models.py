from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify


class Company(models.Model):

    class Meta:
        verbose_name_plural = "companies"
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Product(models.Model):
    company = models.ForeignKey('reviews.Company', on_delete=models.PROTECT, related_name='products')
    name = models.CharField('Product Name', max_length=128)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product-update', kwargs={'pk': self.pk, 'slug': slugify(self.name)})


class Review(models.Model):

    product = models.ForeignKey('reviews.Product', on_delete=models.PROTECT, related_name='reviews')
    comment = models.CharField('Review comment', max_length=128)
    stars = models.IntegerField('Number of stars')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.stars) + " Stars"

    def get_absolute_url(self):
        return reverse('review-update', kwargs={'pk': self.pk})

