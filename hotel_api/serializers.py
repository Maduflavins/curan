from rest_framework import serializers
from hotel_api.models import Booking

class BookingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Booking
        fields = ('booking_id', 'hotel_name', 'customer_name', 'customer_phonenumber', 'location', 'timestamp')
        read_only_fields = ('booking_id', 'timestamp')
