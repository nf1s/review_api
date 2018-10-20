
from api.views import ReviewRudView , CompanyRudView, ProductRudView
from django.conf.urls import url

urlpatterns = [
    url(r'^company/(?P<pk>\d+)/$', CompanyRudView.as_view(), name='company-rud'),
    url(r'^product/(?P<pk>\d+)/$', ProductRudView.as_view(), name='product-rud'),
    url(r'^review/(?P<pk>\d+)/$', ReviewRudView.as_view(), name='review-rud'),

]
