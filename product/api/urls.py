
from api.views import ReviewRudView
from django.conf.urls import url

urlpatterns = [
    url(r'^review/id=(?P<pk>\d+)/$', ReviewRudView.as_view(), name='review-rud'),
]
