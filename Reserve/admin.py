from django.contrib import admin
from .models import Reservation, ReservtionPassenger

admin.site.register(Reservation)
admin.site.register(ReservtionPassenger)