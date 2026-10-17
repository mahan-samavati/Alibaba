import validators
from django.db import models
from Residence.models import Room
from UserProfile.models import User

class Reservation(models.Model):
    room = models.ForeignKey(
        Room,
        on_delete=models.PROTECT,
        related_name="reservation",
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reservation_user'
    )
    start_date = models.DateField()
    end_date = models.DateField()
    guest_number = models.PositiveSmallIntegerField()
    leader_phone_number = models.CharField(
        max_length=11,
        validators=[validators.phone_number_validators]
    )

    @property
    def get_total_price(self):
        day = (self.end_date - self.start_date).days
        return self.room.price * day


class ReservtionPassenger(models.Model):
    class Meta:
        unique_together = ('reservation', 'national_code')

    
    gender = models.CharField(choices=[('زن', 'زن'), ('مرد', 'مرد')])
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    national_code = models.CharField(
        max_length=10,
        validators=[validators.national_code_validators]
    )
    reservation = models.ForeignKey(
        Reservation,
        on_delete=models.CASCADE,
        related_name='passengers'
    )