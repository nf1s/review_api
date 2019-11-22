from api.views import CompanyAPIView
from api.views import CompanyRudView
from api.views import ProductAPIView
from api.views import ProductRudView
from api.views import ReviewAPIView
from api.views import ReviewRudView

from django.conf.urls import url
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Reviews API",
        default_version="v1",
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    url(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    url(
        r"^redoc/$",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
    url(
        r"^company/(?P<pk>\d+)/$", CompanyRudView.as_view(), name="company-rud"
    ),
    url(
        r"^product/(?P<pk>\d+)/$", ProductRudView.as_view(), name="product-rud"
    ),
    url(r"^review/(?P<pk>\d+)/$", ReviewRudView.as_view(), name="review-rud"),
    url(r"^company/$", CompanyAPIView.as_view(), name="company-create"),
    url(r"^product/$", ProductAPIView.as_view(), name="product-create"),
    url(
        r"^product/(?P<pk>\d+)/reviews/$",
        ReviewAPIView.as_view(),
        name="review-create",
    ),
]
