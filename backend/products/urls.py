
from django.urls import path
from .views import ProductList, Health
urlpatterns=[
    path("health/", Health.as_view(), name="health"),
    path("products/", ProductList.as_view(), name="products"),
]
