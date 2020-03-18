from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'bookings', views.BookingView, 'Booking')

urlpatterns = [
    path('', include(router.urls)),
    path(r'properties', views.properties),
    # path(r'properties?at=<str:lat>/<str:long>', views.properties),
    path(r'propertiies/<str:property_id>/bookings', views.property_bookings),
]
