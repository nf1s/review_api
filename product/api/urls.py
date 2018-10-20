
from api.views import CompanyAPIView
from api.views import CompanyRudView
from api.views import ProductAPIView
from api.views import ProductRudView
from api.views import ReviewAPIView
from api.views import ReviewRudView

from django.conf.urls import url

urlpatterns = [
    url(r'^company/(?P<pk>\d+)/$', CompanyRudView.as_view(), name='company-rud'),
    url(r'^product/(?P<pk>\d+)/$', ProductRudView.as_view(), name='product-rud'),
    url(r'^review/(?P<pk>\d+)/$', ReviewRudView.as_view(), name='review-rud'),
    url(r'^company/$', CompanyAPIView.as_view(), name='company-create'),
    url(r'^product/$', ProductAPIView.as_view(), name='product-create'),
    url(r'^review/$', ReviewAPIView.as_view(), name='review-create'),
]
