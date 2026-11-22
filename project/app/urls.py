from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

# yahan se class based api hai
# router = DefaultRouter()

# router.register("products", ProductViewSet)


# urlpatterns = [
#     path("", include(router.urls)),
# ]

# yahan se function based api hai

urlpatterns = [
    path("products/", products),
    path("products/<int:id>/", product_detail),
]