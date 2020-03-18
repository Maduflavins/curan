from django.db import models

# Create your models here.
class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    hotel_name = models.CharField(max_length=45)
    customer_name = models.CharField(max_length=45)
    customer_phonenumber = models.CharField(max_length=20)
    location = models.CharField(max_length=150)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'booking'